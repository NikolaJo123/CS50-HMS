from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def appointment(request):
    return render(request, 'appointment.html', {})
