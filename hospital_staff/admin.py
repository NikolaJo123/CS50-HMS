from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from .models import Staff, Employee, Speciality


# Register your models here.


class StaffAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = ('tree_actions', 'indented_title', 'created_at', 'updated_at')
    list_display_links = ('indented_title',)
    list_filter = ['title']
    prepopulated_fields = {'keywords': ('title',)}


class EmployeeAdmin(admin.ModelAdmin):

    TEXT = "Click on to 'hide' to hide this section."

    list_display = ['user', 'role', 'speciality', 'employed', 'updated_info']
    list_filter = ['user', 'role']
    fieldsets = (
        ('Basic Info', {
            'fields': [('user', 'middlename',), 'birthdate', 'personal_ID_number'],
        }),
        ('Status', {
            'fields': [('role', 'speciality', 'clinic', 'status')]
        }),
        ('Contact Info', {
            'fields': [('phone', 'mobile', 'email')],
            'classes': ('collapse',),
            'description': '%s' % TEXT,
        }),
        ('Address Info', {
            'fields': [('address', 'city', 'country')],
            'classes': ('collapse',),
            'description': '%s' % TEXT,
        }),
        ('Image', {
            'fields': ['user_image'],
            'classes': ('collapse',),
            'description': '%s' % TEXT,
        }),
    )
    #readonly_fields = ['image_tag']


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['department', 'created_at', 'updated_at']
    list_filter = ['department']
    prepopulated_fields = {'keywords': ('department',)}



admin.site.register(Staff, StaffAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Speciality, SpecialityAdmin)
