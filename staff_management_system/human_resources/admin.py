from django.contrib import admin
from .models import Department,Employee

# Register your models here.

class EmplyeeAdmin(admin.ModelAdmin):
    """
    This displays the functionality of the admin page
    """
    # list_display: Controls which fields are displayed on the change list page of the admin.
    list_display = ('first_name','last_name','employee_id','department')

    # list_filter: Enables filtering options on the right sidebar of the change list page.
    # Users can filter by these fields.
    list_filter = ('department', 'employee_id')