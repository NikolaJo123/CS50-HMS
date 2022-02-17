from django.db.models import fields
from django.forms import ModelForm, TextInput, Textarea, widgets, EmailField, EmailInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import models
from django.forms import Select, FileInput

from .models import Patient


class DateInput(forms.DateInput):
    input_type = 'date'


class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = '__all__'
        #labels = {'first_name': '', 'last_name': '', 'username': '', 'email': '', 'password1':'', 'password2':  ''}
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Name'}),
            'surname' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Surname'}),
            'middlename' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Middlename'}),
            'patient_ID': forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Patient ID'}),
            'birthdate': DateInput(),
            'phone' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Phone'}),
            'mobile' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Mobile'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control rounded-left', 'placeholder': 'Email Address'}),
            'address' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Address'}),
            'city' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'City'}),
            'country' : forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-4', 'placeholder': 'Country'}),
        }

'''class PatientForm(forms.ModelForm): 
    class Meta: 
        model = Patient
        fields = '__all__'
        widgets = {
        }

    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }
        )
    )
'''

