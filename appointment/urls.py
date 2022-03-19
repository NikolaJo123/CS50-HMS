from django.urls import path, include
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('appointment/', views.appointment, name='appointment'),

    #API Routes
    path('appointment/patient/', views.patient, name='patient'),
    path('appointment/clinic/', views.clinic, name='clinic'),
    path('appointment/staff/', views.staff, name='staff'),
    path('appointment/makeappointment/', views.makeappointment, name='makeappointment'),
    path('appointment/getappointments/', views.getappointments, name='getappointments'),
    path('appointment/getappointment/<int:id>', views.getappointment, name='getappointment'),
    path('appointment/reappointment/', views.reappointment, name='reappointment'),
    path('appointment/delete/<int:id>', views.delete, name='delete'),
]
