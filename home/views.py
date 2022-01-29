import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from patient.models import Patient

# Create your views here.


def index(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient
    }
    return render(request, 'home.html', context)
