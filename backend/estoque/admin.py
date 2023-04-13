from django.contrib import admin
from .models import *


# def _validate():
#     schema_name = get_current_schema()
#     if schema_name == 'public':
#         return True
#     return False


# class PermissionTenantAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return _validate()

#     def has_delete_permission(self, request, obj=None):
#         return _validate()

#     def has_change_permission(self, request, obj=None):
#         return _validate()


# @admin.register(Category)
# class CategoryAdmin(PermissionTenantAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
