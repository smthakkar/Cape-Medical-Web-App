from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'full_name', 'admin', 'last_login')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin','staff', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

# admin.site.unregister(Group)