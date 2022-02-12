from django.contrib import admin
from home.views import index
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # API Routes
    path('patient/', views.patient, name='patient'),
    path('register_patient/', views.register_patient, name='register_patient'),
]
