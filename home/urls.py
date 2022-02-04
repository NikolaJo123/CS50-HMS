from django.contrib import admin
from home.views import index
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', views.patient, name='patient'),
]
