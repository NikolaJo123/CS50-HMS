from django.contrib import admin
from django.utils.html import format_html

from .models import Patient, PatientExamination, PatientHistory


# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))
    
    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True

    TEXT = "Click on to 'hide' to hide this section."

    list_display = ['name', 'surname', 'middlename', 'patient_ID', 'age', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['name', 'surname', 'patient_ID']
    fieldsets = (
        ('Basic Info', {
            'fields': [('name', 'middlename', 'surname',), 'age', 'patient_ID'],
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
            'fields': ['image', 'image_tag'],
            'classes': ('collapse',),
            'description': '%s' % TEXT,
        }),
    )
    readonly_fields = ['image_tag']


class PatientExaminationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'patient_status', 'prescription', 'doctor', 'examined', 'updated_at']
    list_filter = ['patient', 'patient_status', 'doctor']


class PatientHistoryAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'history']
    list_filter = ['patient', 'doctor']


admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientExamination, PatientExaminationAdmin)
admin.site.register(PatientHistory, PatientHistoryAdmin)
