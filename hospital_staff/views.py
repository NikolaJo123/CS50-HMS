from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Staff, Employee
from .serializers import StaffSerializer, EmployeeSerializer
from .forms import UserUpdateForm, UserContactUpdateForm, UserLocationUpdateForm, UserEmployeeUpdateForm

from core.models import Location, UserContact


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
    contact = Employee.objects.get(user_id = request.user)
    location = Employee.objects.get(user_id = request.user)
    employee = Employee.objects.get(user_id = request.user)
    user_form = UserUpdateForm(instance = request.user)
    contact_form = UserContactUpdateForm(instance = contact)
    location_form = UserLocationUpdateForm(instance = location)
    employee_form = UserEmployeeUpdateForm(instance = employee)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        contact_form = UserContactUpdateForm(request.POST, instance = employee)
        location_form = UserLocationUpdateForm(request.POST, instance = employee)
        employee_form = UserEmployeeUpdateForm(request.POST, request.FILES, instance = employee)

        if (user_form.is_valid() and employee_form.is_valid()) and (location_form.is_valid() and contact_form.is_valid()):
            user_form.save()
            employee_form.save()
            location_form.save()
            contact_form.save()

            return redirect('/profile')
        else:
            return HttpResponse("It doesn't work!!!")
    else:
        context = {
            'contact_form': contact_form,
            'location_form': location_form,
            'employee_form': employee_form,
            'user_form': user_form
        }
        return render(request, "staffprofile.html", context)


def user_update(request):
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


