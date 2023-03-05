from django.urls import path, include
from . import views


urlpatterns = [
    path('medicalstaff/', views.medicalstaff, name='medicalstaff'),
    path('profile/', views.user_profile, name='user_profile'),
    path('userupdate/', views.user_update, name='user_update'),

    # API Routes
    path('getprofile/', views.getprofile, name='getprofile'),
    path('getpersonal/', views.getpersonal, name='getpersonal'),
    path('employees/', views.employees, name='employees'),
    path('getprofession/<int:id>', views.getprofession, name='getprofession'),
]
