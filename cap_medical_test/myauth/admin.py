from django.contrib import admin

from .models import User, Group, SubGroup

# admin.site.register(User)
# admin.site.register(Group)

class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('main_group', 'name')
    ordering = ('main_group', )

admin.site.register(SubGroup, SubGroupAdmin)
# admin.site.register(SubGroup)