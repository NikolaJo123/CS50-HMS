from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls import reverse

from patient.models import Patient
from patient.serializers import PatientSerializer

from hospital_staff.models import Employee
from hospital_staff.serializers import EmployeeSerializer

from clinics.models import Department
from clinics.serializers import DepartmentSerializer

from .models import Appointment
from .serializers import AppointmentSerializer


# Create your views here.


def appointment(request):
    return render(request, 'appointment.html', {})


def patient(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        ser = PatientSerializer(patients, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


def clinic(request):
    if request.method == 'GET':
        patients = Department.objects.all()
        ser = DepartmentSerializer(patients, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


def staff(request):
    if request.method == 'GET':
        patients = Employee.objects.all()
        ser = EmployeeSerializer(patients, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


@csrf_exempt
@login_required
def getappointment(request, id):
    if request.method == 'GET':
        patients = Appointment.objects.filter(patient_id = id)
        ser = AppointmentSerializer(patients, many=True)
        
        return JsonResponse(ser.data, safe=False)
    elif request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)


@csrf_exempt
@login_required
def reappointment(request):
    if request.method == 'POST':
        patientdata = json.loads(request.body)
        appointment_id = patientdata.get("id")
        appointment_object = Appointment.objects.get(id = appointment_id)
        
        #appointment_object.patient = patientdata.get("patient")
        appointment_object.patient_personal_ID = patientdata.get('patient_personal_ID')
        appointment_object.date = patientdata.get('date')
        appointment_object.time = patientdata.get('time')
        appointment_object.doctor_id = patientdata.get('doctor')
        appointment_object.clinic_id = patientdata.get('clinic')
        appointment_object.scheduled_by = request.user
        appointment_object.appointment_reason = patientdata.get('appointment_reason')
        appointment_object.re_apppoinment_reason = patientdata.get('re_apppoinment_reason')

        appointment_object.save()

        return JsonResponse({"message": "Appointment updated successfully"}, status=201)
    elif request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)


@csrf_exempt
@login_required
def delete(request, id):
    if request.method == 'POST':
        patientdata = json.loads(request.body)
        appointment_id = patientdata.get("id")
        appointment_object = Appointment.objects.get(id = appointment_id)
        appointment_object.delete()

        return JsonResponse({"message": "Appointment deleted successfully"}, status=201)
    elif request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)


@csrf_exempt
@login_required
def makeappointment(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    patientdata = json.loads(request.body)
    patient = patientdata.get('patient', "")
    patient_ID = patientdata.get('patient_personal_ID', "")
    date = patientdata.get('date', "")
    time = patientdata.get('time', "")
    doctor = patientdata.get('doctor', "")
    clinic = patientdata.get('clinic', "")
    scheduled_by = patientdata.get('scheduled_by', "")
    appointment_reason = patientdata.get('appointment_reason', "")
    re_apppoinment_reason = patientdata.get('re_apppoinment_reason', "")

    register = Appointment(
        patient_id = patient,
        patient_personal_ID = patient_ID,
        date = date,
        time = time,
        doctor_id = doctor,
        clinic_id = clinic,
        scheduled_by = request.user,
        appointment_reason = appointment_reason,
        re_apppoinment_reason = re_apppoinment_reason,
    )
    register.save()

    return JsonResponse({"message": "Appointment created successfully"}, status=201)


@csrf_exempt
@login_required
def getappointments(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        ser = AppointmentSerializer(appointments, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)

