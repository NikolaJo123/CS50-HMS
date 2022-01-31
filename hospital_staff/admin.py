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
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))
    
    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True

    list_display = ['name', 'surname', 'middlename', 'personal_ID_number', 'employed', 'updated_info', 'image_tag']
    list_filter = ['name', 'surname', 'personal_ID_number']
    readonly_fields = ['image_tag']


admin.site.register(Staff, StaffAdmin)
admin.site.register(Employee, EmployeeAdmin)
