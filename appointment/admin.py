from django.contrib import admin
from django.utils.html import format_html

from .models import Appointment


# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):

    list_display = ['patient', 'patient_personal_ID', 'clinic', 'doctor', 'scheduled_by']
    list_filter = ['patient', 'patient_personal_ID', 'clinic', 'doctor', 'scheduled_by']
    


admin.site.register(Appointment, AppointmentAdmin)
