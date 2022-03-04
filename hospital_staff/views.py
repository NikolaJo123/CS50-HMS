from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Staff, Employee
from .serializers import StaffSerializer, EmployeeSerializer


# Create your views here.


def medicalstaff(request):
    staff = Staff.objects.all()
    return render(request, 'medicalstaff.html', {
        'staff': staff,
})


def getpersonal(request):
    if request.method == 'GET':
        clinics = Staff.objects.all()
        ser = StaffSerializer(clinics, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


def getprofession(request, id):
    if request.method == 'GET':
        #single_staff = Staff
        single_professions = Employee.objects.filter(role_id = id)
        ser = EmployeeSerializer(single_professions, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


def employees(request):
    if request.method == 'GET':
        single_professions = Employee.objects.all()
        ser = EmployeeSerializer(single_professions, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


def user_profile(request):
    context = {
        
    }
    return render(request, "staffprofile.html", context)


def getprofile(request):
    current_user = request.user
    profile = Employee.objects.filter(user_id = current_user.id)
    
    if request.method == 'GET':
        ser = EmployeeSerializer(profile, many=True)
        
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


