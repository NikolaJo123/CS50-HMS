from django.contrib import admin
from home.views import index
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),

    # API Routes
    path('patients/patient/', views.patient, name='patient'),
    path('patients/register_patient/', views.register_patient, name='register_patient'),
]
