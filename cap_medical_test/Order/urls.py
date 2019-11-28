from django.urls import path
from Order.views import index_view, OrderAssignCreate, OrderStatusCreate, report_view

urlpatterns = [
    path('index/', index_view, name='operations'),
    path('report/', report_view, name='reports'),
    path('order_assign/<str:subgroup_name>', OrderAssignCreate, name='order_assign_create'),
    path('order_status/<str:subgroup_name>', OrderStatusCreate, name='order_status_create'),
    # path('order_assign/assign_to/', assign_orders, name='order_assign'),
]