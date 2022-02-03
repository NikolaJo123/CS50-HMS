from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    patient_ID = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
  

class PatientExamination(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_status = models.CharField(max_length=255)
    prescription = models.TextField()
    staff_sign = models.ImageField(blank=True, upload_to='images/')
    examined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.name


class PatientHistory(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    history = models.ForeignKey('patient.PatientExamination', on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name

