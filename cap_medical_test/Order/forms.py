from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from datetime import datetime, timedelta

from django.contrib.auth.models import Group, User
from easy_select2 import Select2Multiple, Select2

from Order.models import Teamsettings1, SalesOrder_new, sales_order_assign
from myauth.models import SubGroup


class RulesCreate(forms.ModelForm):
    class Meta:
        model = Teamsettings1
        MY_COLS = [[i.name,]*2 for i in SalesOrder_new._meta.get_fields()]
        fields = '__all__'
        widgets = {
            # 'main_group' : forms.TextInput(),
            'sharewith' : forms.SelectMultiple(attrs={'class':'js-example-responsive'}),
            # 'sub_group' : forms.ModelChoiceField(queryset=Teamsettings1.objects.filter(maingroup=self.maingroup).select_related('sub_groups')),
            'columnsinclusions' : forms.SelectMultiple(attrs={'class':'js-example-responsive'}, choices=MY_COLS),
            'statusvalidation' : forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'description' : forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'salesorderclassification' : forms.Textarea(attrs={'rows': 4}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_group'].queryset = SubGroup.objects.none()
        if 'main_group' in self.data:
            try:
                main_group_id = int(self.data.get('main_group'))
                self.fields['sub_group'].queryset = SubGroup.objects.filter(main_group_id=main_group_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            # main_group_id = int(self.data.get('main_group'))
            self.fields['sub_group'].queryset = SubGroup.objects.filter(main_group_id=int(self.instance.main_group_id)).order_by('name')
            # self.fields['sub_group'].queryset = self.instance.main_group.sub_group_set.order_by('name')

class FieldSet(object):
    pass


class CreateRules(forms.Form):
    MY_CHOICES = [(i.name,)*2 for i in SalesOrder_new._meta.get_fields()]
    MY_COLS = [[i.name,]*2 for i in SalesOrder_new._meta.get_fields()]
    MY_FUNCT = [('__contains', 'Contains'), ('__startswith', 'Starts With'), ('__endswith', 'Ends With'),
                ('__exact','Exact'), ('__iexact','Incasesensitive Exact'), ('__gt', 'Grater than'),
                ('__gte','Greate than Or Equal to'), ('__lt','Less than'), ('__lte','Less than Or Eqal to'),
                ('__isstartswith','Is Starts With'),('__gte = datetime.now() - timedelta(days = ','Before Days'),
                ('__gte = datetime.now() - timedelta(months = ', 'Before Months'),
                ('__gte = datetime.now() - timedelta(years = ', 'Before Years'),
                ('__isnull = True', 'IS NULL'), ('__isnull = False', 'IS NOT NULL')
                ]

    from django.contrib.auth.models import Group
    # main_grp_choices = [(i.name,)*2 for i in Group.objects.all()]
    # main_group = forms.ChoiceField(choices=main_grp_choices)
    # sharewith = forms.CharField(widget=forms.Textarea(attrs={'cols':40, 'rows':2}))
    # sub_group = forms.CharField(widget=forms.TextInput(attrs={'cols': 80, 'rows': 20}))
    # columnsinclusions = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'js-example-responsive'}), choices=MY_CHOICES)
    # statusvalidation = forms.CharField(widget=forms.TextInput(attrs={'cols': 80, 'rows': 20}))
    columnlist = forms.ChoiceField(label='',choices=MY_CHOICES)
    functionlist = forms.ChoiceField(label='',choices=MY_FUNCT)
    matchvalue = forms.CharField(label='',widget=forms.TextInput())
    # salesorderclassification = forms.CharField(label='Generated Query',widget=forms.Textarea(attrs={'cols': 40, 'rows': 4}))


    class Meta:
        fieldsets = (
            ('Make a Query',{
                'fields': ('columnlist', 'functionlist', 'matchvalue')
            })
        )



class CreateOrderAssign(forms.ModelForm):
    class Meta:
        # STATUSVALIDATIONS = [(i,)*2 for i in Teamsettings1.objects.get(pk=SalesOrder_new.objects.get(pk=sales_order_number).rule_id).statusvalidation.split(',')]
        model = sales_order_assign
        fields = ['assign_to',]

    def __init__(self,subgroup_name, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.is_staff = kwargs.pop('is_staff', None)
        self.uid = kwargs.pop('uid', None)
        super().__init__(*args, **kwargs)
        if subgroup_name:
            try:
                if not self.is_staff:
                    self.fields['assign_to'].choices = [(None,'---------'),(self.uid,self.user),]
                else:
                    # id = Teamsettings1.objects.filter(sub_group__name=subgroup_name)
                    users = Teamsettings1.objects.filter(sub_group__name=subgroup_name).values('sharewith__id')
                    self.fields['assign_to'].queryset = User.objects.all().filter(id__in=users)
            except Exception as e:
                print(str(e))



class CreateOrderStatus(forms.ModelForm):
    class Meta:
        model = sales_order_assign
        fields = ['status',]

    def __init__(self,subgroup_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if subgroup_name:
            try:
                id = Teamsettings1.objects.filter(sub_group__name=subgroup_name)
                statusvalidations = id.values_list('statusvalidation',flat=True)
                temp = list([(i.strip(),)*2 for i in statusvalidations[0].split(',')])
                temp1 = [(None,'-----------')]
                temp1.extend(temp)
                self.fields['status'].choices = temp1
            except Exception as e:
                print(str(e))