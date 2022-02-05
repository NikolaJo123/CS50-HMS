from django.contrib import admin
from django.utils.html import format_html

from .models import Department


# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'created_at', 'updated_at']
    list_filter = ['department_name']
    prepopulated_fields = {'keywords': ('department_name',)}


admin.site.register(Department, DepartmentAdmin)
