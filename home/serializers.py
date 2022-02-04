from rest_framework import serializers
from patient.models import Patient


class AppointmentSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(source='user.username')

    class Meta:
        model = Patient
        fields = ('id', 'name', 'middlename', 'surname', 
                'patient_ID', 'age', 'phone', 'mobile', 
                'email', 'address', 'city', 'country')

