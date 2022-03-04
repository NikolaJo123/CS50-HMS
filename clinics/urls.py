from django.urls import path, include
from . import views


urlpatterns = [
    path('clinics/', views.clinicspage, name='clinicspage'),
    path('clinics/clinicpage/<int:id>', views.clinic, name='clinic'),
    
    # API Routes
    path('getclinics/', views.getclinics, name='getclinics'),
]