from rest_framework import serializers
from .models import Appointment



class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name')
    patient_surname = serializers.CharField(source='patient.surname')
    patient_middlename = serializers.CharField(source='patient.middlename')
    doctor_name = serializers.CharField(source='doctor.first_name')
    doctor_surname = serializers.CharField(source='doctor.last_name')
    clinic_name = serializers.CharField(source='clinic.department_name')
    scheduled_by_name = serializers.CharField(source='scheduled_by.first_name')
    scheduled_by_surname = serializers.CharField(source='scheduled_by.last_name')

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'patient_name', 'patient_surname', 'patient_middlename', 'patient_personal_ID',
                'time', 'date', 'doctor', 'doctor_name', 'doctor_surname',
                'clinic', 'clinic_name',
                'scheduled_by', 'scheduled_by_name', 'scheduled_by_surname',
                'appointment_reason', 're_apppoinment_reason', 'appointed_at', 'updated_at')

