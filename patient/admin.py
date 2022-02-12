from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Patient, PatientExamination, PatientHistory, Testmodel


# Register your models here.


class PatientAdmin(admin.ModelAdmin):  

    TEXT = "Click on to 'hide' to hide this section."

    list_display = ['name', 'surname', 'middlename', 'patient_ID', 'age', 'created_at', 'updated_at']
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
    )


class PatientExaminationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'patient_status', 'prescription', 'doctor', 'examined', 'updated_at']
    list_filter = ['patient', 'patient_status', 'doctor']


class PatientHistoryAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'history']
    list_filter = ['patient', 'doctor']


class TestmodelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientExamination, PatientExaminationAdmin)
admin.site.register(PatientHistory, PatientHistoryAdmin)
admin.site.register(Testmodel, TestmodelAdmin)
