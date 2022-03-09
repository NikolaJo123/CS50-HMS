from django import forms
from django.forms import TextInput, DateInput, EmailInput, Select, FileInput, DateTimeInput, DateTimeField, DateField, ModelChoiceField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User
from core.models import UserContact, Location
from clinics.models import Department
from .models import Employee, Speciality, Staff


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class UserContactUpdateForm(UserChangeForm):
    class Meta:
        model = UserContact
        fields = ('phone', 'mobile', 'email')
        widgets = {
            'phone' : TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'mobile' : TextInput(attrs={'class': 'input', 'placeholder': 'Mobile'}),
            'email' : EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
        }


class UserEmployeeUpdateForm(UserChangeForm):
    #user_image = forms.ImageField()
    birthdate = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datetimepicker-input',
                'type': 'date'
            }
        ))
    
    speciality = ModelChoiceField(
        queryset = Speciality.objects.all()
        )

    clinic = ModelChoiceField(
        queryset = Department.objects.all())

    role = ModelChoiceField(
        queryset = Staff.objects.all()
        )

    class Meta:
        model = Employee
        fields = ('middlename', 'birthdate', 'personal_ID_number', 'speciality', 'clinic', 'role', 'user_image')
        widgets = {
            'middlename' : TextInput(attrs={'class': 'input', 'placeholder': 'Middlename'}),
            'personal_ID_number' : TextInput(attrs={'class': 'input', 'placeholder': 'Personal ID'}),
            'user_image' : FileInput(attrs={'class': 'input', 'placeholder': 'Image'}),
        }  


class UserLocationUpdateForm(UserChangeForm):
    class Meta:
        model = Location
        fields = ('address', 'city', 'country')
        widgets = {
            'address' : TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'city' : TextInput(attrs={'class': 'input', 'placeholder': 'City'}),
            'country' : TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
        }

