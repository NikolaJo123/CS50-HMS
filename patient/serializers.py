from rest_framework import serializers
from patient.models import Patient, PatientExamination, PatientHistory


# Create your serializers here.


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'name', 'middlename', 'surname', 
                'patient_ID', 'birthdate', 'phone', 'mobile', 
                'email', 'address', 'city', 'country')


class PatientExaminationSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name')
    patient_surname = serializers.CharField(source='patient.surname')
    patient_middlename = serializers.CharField(source='patient.middlename')
    patient_ID = serializers.CharField(source='patient.patient_ID')

    doctor_name = serializers.CharField(source='doctor.username')

    class Meta:
        model = PatientExamination
        fields = ('id', 'patient', 'patient_name', 'patient_surname', 
                'patient_middlename', 'patient_ID', 'doctor_name', 'patient_status', 
                'prescription', 'examined', 'updated_at')


class PatientHistorySerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name')
    patient_surname = serializers.CharField(source='patient.surname')
    patient_middlename = serializers.CharField(source='patient.middlename')
    patient_ID = serializers.CharField(source='patient.patient_ID')

    doctor_name = serializers.CharField(source='doctor.username')

    patient_history = serializers.CharField(source='history.patient_status')

    class Meta:
        model = PatientHistory
        fields = ('id', 'patient', 'doctor', 'patient_name', 'patient_surname', 
                'patient_middlename', 'patient_ID', 'doctor_name', 'patient_history',)

