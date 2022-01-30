from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from .models import Hospital_Staff


# Register your models here.


class HospitalStaffAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    #list_display = ['title', 'created_at', 'updated_at']
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    list_filter = ['title']
    prepopulated_fields = {'keywords': ('title',)}


admin.site.register(Hospital_Staff, HospitalStaffAdmin)