import concurrent

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

from Order.decorators import user_is_staff
from Order.models import sales_order_assign as order_assign
from Order.models import assign_history as order_hist
from Order.models import SalesOrder_new as master
from Order.models import Teamsettings1 as setting
from Order.forms import RulesCreate, CreateRules, CreateOrderAssign, CreateOrderStatus

from myauth.models import SubGroup
# Create your views here.


def apply_rules(request):
    # all_orders = master.objects.filter(Q(sales_order_confirm_date__isnull = True))
    master.objects.all().update(rule = None)
    all_rules = setting.objects.all().values_list('conditions', 'id').order_by('id')
    for i,id in all_rules:
        all_orders = master.objects.filter(Q(sales_order_confirm_date__isnull=True))
        i = i.replace('AND','&').replace('OR','|')
        # i = "Q(" + i.replace("  ", " ").replace(" AND ", ") & Q(") + ")"
        sales_orders = all_orders.filter(rule__exact = None).filter(eval(i)).update(rule=id)
    return redirect('teamsettings')


def check_change_status(user,order_num):
    order = master.objects.filter(pk=order_num)
    user = User.objects.get(pk=user)
    if not user.is_staff:
        if order.values_list('sales_order_assign__assign_to__username')[0][0] == user.username:
            return True
        else:
            return False
    else:
        return True


@login_required
def OrderAssignCreate(request, subgroup_name):
    order_numbers = request.POST.getlist('sales_order_number')

    if order_numbers == [] and request.POST['assign_to']:
        # request.POST.pop('csrfmiddlewaretoken')
        assign_to = request.POST['assign_to']
        sales_orders = eval(request.POST['sales_orders'])

        for sales_order in sales_orders:
            sales_order = int(sales_order)
            obj = order_assign.objects.filter(pk=sales_order)
            if obj:
                if request.user.is_staff:
                    ob_update = obj.update(assign_to=User(pk=assign_to))
                    order_hist.objects.create(sales_order=sales_order, assigned_by=request.user, assigned_to=User.objects.get(pk=assign_to).username)
            else:
                obj_create = order_assign.objects.create(pk=sales_order, assign_to=User(pk=assign_to))
                order_hist.objects.create(sales_order=sales_order, assigned_by=request.user, assigned_to=User.objects.get(pk=assign_to).username)
        else:
            return redirect('operations')

        print(request.POST['assign_to'])

    form = CreateOrderAssign(subgroup_name,user=request.user,is_staff=request.user.is_staff, uid=request.user.id)
    context = {
        'form':form,
        'order_numbers':order_numbers
    }
    return render(request, 'Order/order_assign_create.html', context)


@login_required
def OrderStatusCreate(request, subgroup_name):
    # elif request.POST['action'] == 'Change Status':
    order_numbers = request.POST.getlist('sales_order_number')

    if order_numbers == [] and request.POST['status']:
        # request.POST.pop('csrfmiddlewaretoken')
        status = request.POST['status']
        sales_orders = eval(request.POST['sales_orders'])

        for sales_order in sales_orders:
            sales_order = int(sales_order)
            if check_change_status(request.user.id, sales_order):
                obj = order_assign.objects.filter(pk=sales_order)
                if obj:
                    obj_update = obj.update(status=status)
                    order_hist.objects.create(sales_order=sales_order, assigned_by=request.user, status=status)
                else:
                    obj_create = order_assign.objects.create(pk=sales_order, status=status)
                    order_hist.objects.create(sales_order=sales_order, assigned_by=request.user, status=status)
        else:
            return redirect('operations')

    form = CreateOrderStatus(subgroup_name)
    context = {
        'form': form,
        'order_numbers': order_numbers
    }
    return render(request, 'Order/order_status.html', context)


@login_required
def assign_orders(request):
    if request.method == 'POST':
        form = CreateOrderAssign(request.POST)
        if form.is_valid():
            print('=========================================')
            print(form.cleaned_data)



def load_sub_groups(request):
    main_group_id = request.GET.get('main_group')
    sub_groups = SubGroup.objects.filter(main_group_id=main_group_id).order_by('name')
    return render(request, 'hr/sub_group_dropdown_list_options.html', {'sub_groups': sub_groups})


@method_decorator(user_is_staff, name='dispatch')
class RulesCreateView(LoginRequiredMixin,CreateView):
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."
    def get(self, request, *args, **kwargs):
        form2 = CreateRules()
        context = {'form': RulesCreate(), 'form2':form2}
        return render(request, 'Order/rules_create.html', context)

    def post(self, request, *args, **kwargs):
        form = RulesCreate(request.POST)
        print('================form============================')
        # print(form.cleaned_data)
        if form.is_valid():
            print('================ form valid=================')
            # data = form.cleaned_data
            # data['salesorderclassification'] = data['salesorderclassification']
            # rule = setting.objects.create(**data)
            rule = form
            rule.save()
            return HttpResponseRedirect(reverse('teamsettings'))
        else:
            print(form.errors)
        return render(request, 'Order/rules_create.html', {'form':form})



@method_decorator(user_is_staff, name='dispatch')
class RuleDeleteView(LoginRequiredMixin,DeleteView):
    model = setting
    success_url = reverse_lazy('teamsettings')
    template_name = 'Order/rule_delete.html'
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(setting, id=id_)



@method_decorator(user_is_staff, name='dispatch')
class RuleEditView(LoginRequiredMixin,UpdateView):
    template_name = 'Order/rule_edit.html'
    form_class = RulesCreate
    success_url = reverse_lazy('teamsettings')
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(setting, id=id_)

    # def get_initial(self):
    #     initial = super(RuleEditView, self).get_initial()
    #     print('=========================================')
    #     print(initial)
    #     rule_obj = self.get_object()
    #     initial['main_group'] = rule_obj.main_group
    #     initial['sub_group'] = rule_obj.sub_group
    #     initial['sharewith'] = rule_obj.sharewith
    #     initial['columnsinclusions'] = rule_obj.columnsinclusions
    #     initial['description'] = rule_obj.description
    #     initial['statusvalidation'] = rule_obj.statusvalidation
    #     initial['salesorderclassification'] = rule_obj.statusvalidation
    #     return initial

    def form_valid(self, form):
        return super().form_valid(form)


@login_required
def index_view(request):
    if request.user.is_authenticated:
        all_ids = setting.objects.values_list('id', flat=True)
        all_results = {}
        ordered = master.objects.select_related('rule').all()

        for i in all_ids:
            obj = setting.objects.get(pk=i)
            users = obj.sharewith.all()
            try:
                if request.user.is_staff:
                    r = master.objects.filter(rule__exact=i).values('sales_order_assign__status').annotate(total=Count('sales_order_assign__status')).order_by('total')
                    result_set = ordered.filter(rule__exact=i).values(*str('sales_order_assign__status,sales_order_assign__assign_to__username,sales_order_number,'+obj.columnsinclusions.replace('\r\n','').replace("'","").replace('[','').replace(']','').replace(', ',',').replace(' ','_').lower()).split(','))
                else:
                    result_set = ordered.filter(Q(sales_order_assign__assign_to__username = request.user.username) | Q(sales_order_assign__assign_to__username = None)).filter(rule__exact=i).values(*str('sales_order_assign__status,sales_order_assign__assign_to__username,sales_order_number,'+obj.columnsinclusions.replace('\r\n','').replace("'","").replace('[','').replace(']','').replace(', ',',').replace(' ','_').lower()).split(','))
            except Exception as e:
                result_set = None
                print(str(e))

            if result_set:
                try:
                    all_results[obj.main_group][obj.sub_group] = result_set
                except KeyError as e:
                    all_results[obj.main_group]={}
                    all_results[obj.main_group][obj.sub_group] = result_set
            else:
                try:
                    all_results[obj.main_group][obj.sub_group] = []
                except KeyError as e:
                    all_results[obj.main_group] = {}
                    all_results[obj.main_group][obj.sub_group] = list(result_set)

        context = {
            'resultset':all_results,
            # 'all':User.all_users()
        }
        return render(request, 'Order/index.html', context)
    else:
        return redirect('/accounts/login/')



def report_view(request):
    if request.user.is_authenticated:
        all_ids = setting.objects.values_list('id', flat=True)
        all_results = {}
        ordered = master.objects.select_related('rule').all()

        for i in all_ids:
            obj = setting.objects.get(pk=i)
            users = obj.sharewith.all()
            try:
                if request.user.is_staff:
                    r = master.objects.filter(rule__exact=i).values('sales_order_assign__status').annotate(
                        total=Count('sales_order_assign__status')).order_by('total')
                    result_set = ordered.filter(rule__exact=i).values(*str(
                        'sales_order_assign__status,sales_order_assign__assign_to__username,sales_order_number,' + obj.columnsinclusions.replace(
                            '\r\n', '').replace("'", "").replace('[', '').replace(']', '').replace(', ', ',').replace(
                            ' ', '_').lower()).split(','))
                else:
                    result_set = ordered.filter(Q(sales_order_assign__assign_to__username=request.user.username) | Q(
                        sales_order_assign__assign_to__username=None)).filter(rule__exact=i).values(*str(
                        'sales_order_assign__status,sales_order_assign__assign_to__username,sales_order_number,' + obj.columnsinclusions.replace(
                            '\r\n', '').replace("'", "").replace('[', '').replace(']', '').replace(', ', ',').replace(
                            ' ', '_').lower()).split(','))
            except Exception as e:
                result_set = None
                print(str(e))

            if result_set:
                try:
                    # all_results[obj.main_group][obj.sub_group] = result_set
                    all_results[obj.main_group][obj.sub_group]['res_set'] = result_set
                except KeyError as e:
                    all_results[obj.main_group] = {}
                    all_results[obj.main_group][obj.sub_group] = {}
                    all_results[obj.main_group][obj.sub_group]['res_set'] = result_set
            else:
                try:
                    all_results[obj.main_group][obj.sub_group]['res_set'] = []
                except KeyError as e:
                    all_results[obj.main_group] = {}
                    all_results[obj.main_group][obj.sub_group] = {}
                    all_results[obj.main_group][obj.sub_group]['res_set'] = list(result_set)

        context = {
            'resultset': all_results,
            # 'all':User.all_users()
        }
        return render(request, 'Order/report.html', context)
    else:
        return redirect('/accounts/login/')


def home_view(request):
    if request.user.is_authenticated:
        return redirect('/sales/index/')
    else:
        return redirect('/accounts/login/')


@login_required
def dashboard_view(request):

    context = {
    }
    return render(request, 'Order/dashboard.html', context)


@login_required
@user_is_staff
def s_view(request):
    setting_table = setting.objects.all()

    temp = list(setting_table)
    context={
        'resultset':setting_table,
        # 'columns': list(setting._meta._fields())
    }
    return render(request,'Order/settings.html', context)
