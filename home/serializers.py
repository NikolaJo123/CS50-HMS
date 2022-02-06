from rest_framework import serializers
from patient.models import Patient, PatientExamination, PatientHistory
from clinics.models import Department
from hospital_staff.models import Speciality, Employee, Staff


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'name', 'middlename', 'surname', 
                'patient_ID', 'age', 'phone', 'mobile', 
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


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'department_name', 'description', 'created_at', 'updated_at')


class SpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = ('id', 'department', 'keywords', 'description', 'created_at', 'updated_at')


class EmployeeSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='user.username')
    employee_surname = serializers.CharField(source='user.last_name')
    role = serializers.CharField(source='role.title')
    speciality = serializers.CharField(source='speciality.department')

    class Meta:
        model = Employee
        fields = ('id', 'user', 'employee_name', 'employee_surname', 'middlename', 
                'role', 'speciality', 'personal_ID_number', 'status', 'birthdate',
                'user_image', 'employed', 'updated_info')


class StaffSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent')

    class Meta:
        model = Staff
        fields = ('id', 'parent', 'parent_name', 'title', 'keywords', 'description',
                'created_at', 'updated_at')

