from django.shortcuts import render
from django.urls import reverse
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from patient.models import Patient
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from .serializers import AppointmentSerializer


# Create your views here.


def index(request):
    #patient = Patient.objects.all()
    #context = {'patient': patient}
    #return render(request, 'index.html', context)

    if request.method == 'GET':
        patients = Patient.objects.all()
        ser = AppointmentSerializer(patients, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)
