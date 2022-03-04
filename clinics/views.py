from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Department
from .serializers import DepartmentSerializer


# Create your views here.


def clinicspage(request):

    return render(request, 'clinics.html', {
    })


def clinic(request, id):
    clinicprofile = Department.objects.get(id = id)
    context = {
        'clinic': clinicprofile
    }

    return render(request, 'single_clinic.html', context)


def getclinics(request):
    if request.method == 'GET':
        clinics = Department.objects.all()
        ser = DepartmentSerializer(clinics, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)

