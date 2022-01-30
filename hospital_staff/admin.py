from django.contrib import admin
from django.utils.html import format_html

from .models import Hospital_Staff


# Register your models here.


class HospitalStaffAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['title']


admin.site.register(Hospital_Staff, HospitalStaffAdmin)