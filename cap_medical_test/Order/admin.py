from django.contrib import admin
from .models import Teamsettings1, SalesOrder_new, assign_history

# Register your models here.

admin.site.register(SalesOrder_new)
admin.site.register(Teamsettings1)

class assign_historyAdmin(admin.ModelAdmin):
    list_display = ('sales_order', 'assigned_by', 'assigned_to', 'status', 'assign_time')
    search_fields = ('sales_order', 'assigned_by', 'assigned_to', 'status', 'assign_time')


admin.site.register(assign_history, assign_historyAdmin)