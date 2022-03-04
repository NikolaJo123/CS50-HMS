"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from home.views import index
from home import views as HomeViews
from appointment.views import appointment
from hospital_staff.views import medicalstaff
from clinics import views as ClinicView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', include('home.urls')),
    path('patients/', HomeViews.patients, name='patients'),
    path('admin/', admin.site.urls),
    path('', include('appointment.urls')),
    path('', include('hospital_staff.urls')),
    path('', include('clinics.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
