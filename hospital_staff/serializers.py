from rest_framework import serializers
from .models import Speciality, Employee, Staff



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

