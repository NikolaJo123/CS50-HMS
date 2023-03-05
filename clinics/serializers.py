from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ('id', 'parent', 'department_name', 'description', 'created_at', 'updated_at')

