from django.contrib import admin
from home.views import index
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("treatment/", views.treatment, name="treatment"),

    # API Routes
    path('patients/patient/', views.patient, name='patient'),
    path('patients/register_patient/', views.register_patient, name='register_patient'),
    path('treatment/get_treatment/', views.get_treatment, name='get_treatment'),
    path('treatment/get_single_treatment/<int:id>', views.get_single_treatment, name='get_single_treatment'),
    path('treatment/get_single_patient/<int:id>', views.get_single_patient, name='get_single_patient'),
]
