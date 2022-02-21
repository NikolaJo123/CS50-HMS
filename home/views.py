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
from django.contrib.auth.models import User

from .forms import LoginForm, SignUpForm

from patient.forms import PatientForm
from patient.models import Patient, PatientExamination, PatientHistory
from patient.serializers import *

from clinics.models import Department

from hospital_staff.models import Speciality, Employee, Staff

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
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    msg = None
    success = False
    
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            msg = 'User created successfully!'
            success = True

            return HttpResponseRedirect('/')
        else:
            msg = 'Invalid Credentials!'
    else:
        form = SignUpForm()
    
    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


    '''# Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "accounts/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "accounts/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})'''
    


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
