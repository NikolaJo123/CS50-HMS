from rest_framework import serializers
from .models import Speciality, Employee, Staff



class SpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = ('id', 'department', 'keywords', 'description', 'created_at', 'updated_at')


class EmployeeSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='user.first_name')
    employee_surname = serializers.CharField(source='user.last_name')
    role_title = serializers.CharField(source='role.title')
    speciality_name = serializers.CharField(source='speciality.department')
    cninic_name = serializers.CharField(source='clinic.department_name')

    class Meta:
        model = Employee
        fields = ('user', 'employee_name', 'employee_surname', 'middlename', 
                'role', 'role_title', 'speciality', 'speciality_name', 'clinic', 'cninic_name',
                'personal_ID_number', 'status', 'birthdate',
                'email', 'phone', 'mobile', 'address', 'city', 'country',
                'user_image', 'employed', 'updated_info')


class StaffSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent')

    class Meta:
        model = Staff
        fields = ('id', 'parent', 'parent_name', 'title', 'keywords', 'description',
                'created_at', 'updated_at')

