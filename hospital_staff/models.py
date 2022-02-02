from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from django.contrib.auth.models import User
from core.models import Location, UserData, UserContact


# Create your models here.


class Staff(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class MPTTMeta:
        order_insertion_by = ['title']


class Employee(Location, UserData, UserContact):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Blocked', 'Blocked')
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey('hospital_staff.Staff', blank=True, on_delete=models.CASCADE)
    personal_ID_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS)
    #employee_ID = models.CharField(max_length=10)
    employed = models.DateTimeField(auto_now_add=True)
    updated_info = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


