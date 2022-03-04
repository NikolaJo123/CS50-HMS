from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from core.decorators import unauthenticated_user
from django.contrib.auth.models import User, Group

from .forms import LoginForm, SignUpForm

from patient.forms import PatientForm
from patient.models import Patient, PatientExamination, PatientHistory
from patient.serializers import *

from clinics.models import Department

from hospital_staff.models import Speciality, Staff, Employee

from .serializers import *


# Create your views here.


def index(request):

     # Authenticated users view their inbox
    if request.user.is_authenticated:
        form = PatientForm
        context = {'form': form }
        return render(request, 'index.html', context)
    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))


@unauthenticated_user
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                current_user =request.user
                userprofile=Employee.objects.get(user_id=current_user.id)
                request.session['userimage'] = userprofile.user_image.url
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@unauthenticated_user
def register(request):
    msg = None
    success = False

    group_list = Group.objects.all()
    role_list = Staff.objects.all()
    speciality_list = Speciality.objects.all()
    clinic_list = Department.objects.all()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            group_choice = request.POST["group"]
            role_choice = request.POST["role"]
            speciality_choice = request.POST["speciality"]
            clinic_choice = request.POST["clinic"]
            pesonal_ID = request.POST["id-number"]

            if group_choice == 'none':
                msg = 'You need to Enter your medical group in order to continue!'
            
            elif role_choice == 'none':
                msg = 'You need to Enter your medical role in order to continue!'
                
            elif speciality_choice == 'none':
                msg = 'You need to Enter your medical speciality in order to continue!'
                
            elif clinic_choice == 'none':
                msg = 'You need to Enter your clinic in order to continue!'''

            else:
                user = form.save()
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")
                reg_user = authenticate(username=username, password=raw_password)

                group = Group.objects.get(name=group_choice)
                user.groups.add(group)
                login(request, reg_user)
                

                current_user = request.user
                employee = Employee()
                employee.user_id = current_user.id
                employee.personal_ID_number = pesonal_ID
                employee.role_id = int(role_choice)
                employee.speciality_id = int(speciality_choice)
                employee.clinic_id = int(clinic_choice)
                employee.user_image = 'images/emptyuser.jpg'
                employee.save()

                msg = 'User created successfully!'
                success = True

                return HttpResponseRedirect('/')
        else:
            msg = 'Invalid Credentials!'
    else:
        form = SignUpForm()
    
    context = {
        "form": form,
        'group_list': group_list,
        'role_list': role_list,
        'speciality_list': speciality_list,
        'clinic_list': clinic_list,
        "msg": msg,
        "success": success
        }
    return render(request, "accounts/register.html", context)


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

