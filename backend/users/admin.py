from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User = get_user_model()

# admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    
    list_display = ['cpf', 'admin', 'publisher', 'created_at', 'updated_at']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        ('Permissions', {'fields': ('admin','publisher')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'admin', 'publisher')}
        ),
    )
    search_fields = ['cpf']
    ordering = ['cpf']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)