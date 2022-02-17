from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from patient.forms import PatientForm
from patient.models import Patient, PatientExamination, PatientHistory
from patient.serializers import *

from clinics.models import Department

from hospital_staff.models import Speciality, Employee, Staff

from .serializers import *


# Create your views here.


def index(request):
    form = PatientForm
    context = {'form': form }
    return render(request, 'index.html', context)


def patients(request):
    
    return render(request, 'patient.html', {})


def patient(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        ser = PatientSerializer(patients, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


@csrf_exempt
@login_required
def register_patient(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    patientdata = json.loads(request.body)
    name = patientdata.get('name', "")
    surname = patientdata.get('surname', "")
    middlename = patientdata.get('middlename', "")
    patient_ID = patientdata.get('patient_ID', "")
    birthdate = patientdata.get('birthdate', "")
    phone = patientdata.get('phone', "")
    mobile = patientdata.get('mobile', "")
    email = patientdata.get('email', "")
    address = patientdata.get('address', "")
    city = patientdata.get('city', "")
    country = patientdata.get('country', "")

    register = Patient(
        name = name,
        surname = surname,
        middlename = middlename,
        patient_ID = patient_ID,
        birthdate = birthdate,
        phone = phone,
        mobile = mobile,
        email = email,
        address = address,
        city = city,
        country = country
    )
    register.save()

    return JsonResponse({"message": "Patient registered successfully"}, status=201)
