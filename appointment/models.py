from django.db import models

from hospital_staff.models import Staff, Employee
from clinics.models import Department
from patient.models import Patient
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='Patient', on_delete=models.CASCADE)
    patient_personal_ID = models.CharField(max_length=15)
    time = models.CharField(max_length=50)
    date = models.DateField('appointment_date', auto_now=False, auto_now_add=False)
    doctor = models.ForeignKey(User, related_name='Doctor', on_delete=models.CASCADE)
    clinic = models.ForeignKey('clinics.Department', related_name='Department', on_delete=models.CASCADE)
    scheduled_by = models.ForeignKey(User, related_name='Appointed', on_delete=models.CASCADE)
    appointment_reason = models.CharField(max_length=100)
    re_apppoinment_reason = models.CharField(max_length=255, blank=True, null=True)
    appointed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.name

