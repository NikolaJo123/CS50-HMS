from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from .models import Staff, Employee


# Register your models here.


class StaffAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    list_filter = ['title']
    prepopulated_fields = {'keywords': ('title',)}


class EmployeeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.user_image.url))
    
    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True

    TEXT = "Click on to 'hide' to hide this section."

    list_display = ['user', 'role', 'employed', 'updated_info', 'image_tag']
    list_filter = ['user', 'role']
    fieldsets = (
        ('Basic Info', {
            'fields': [('user', 'middlename',), 'birthdate', 'personal_ID_number'],
        }),
        ('Status', {
            'fields': [('role', 'status')]
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
            'fields': ['user_image', 'image_tag'],
            'classes': ('collapse',),
            'description': '%s' % TEXT,
        }),
    )
    readonly_fields = ['image_tag']


admin.site.register(Staff, StaffAdmin)
admin.site.register(Employee, EmployeeAdmin)
