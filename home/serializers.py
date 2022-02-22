from rest_framework import serializers
from clinics.models import Department



class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'department_name', 'description', 'created_at', 'updated_at')

