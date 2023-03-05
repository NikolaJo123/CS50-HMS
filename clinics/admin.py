from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from .models import Department


# Register your models here.


class DepartmentAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'department_name'
    list_display = ('tree_actions', 'indented_title', 'department_name', 'created_at', 'updated_at')
    list_display_links = ('indented_title',)
    list_filter = ['department_name']
    prepopulated_fields = {'keywords': ('department_name',)}


admin.site.register(Department, DepartmentAdmin)
