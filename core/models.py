from django.db import models


# Create your models here.


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    address = models.CharField(blank=True, null=True, max_length=200)
    city = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=50)


class UserContact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)


class UserData(models.Model):
    data_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)  #
    surname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField('birthdate', blank=True, null=True, auto_now=False, auto_now_add=False)
    user_image = models.ImageField(blank=True, upload_to='images/')


