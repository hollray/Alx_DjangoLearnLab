from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Department, Employee, Role, CustomUser

# Register your non-user models
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_id', 'department')
    list_filter = ('department', 'employee_id')

# Register the CustomUser model with a custom admin view.
# This replaces all previous attempts to register the default User model.
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    # Add the 'role' field to the list of fields shown in the admin.
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    # Add the 'role' field to the list display in the admin.
    list_display = BaseUserAdmin.list_display + ('role',)
