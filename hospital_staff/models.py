from statistics import mode
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# Create your models here.


class Hospital_Staff(MPTTModel):
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


class Employee(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Blocked', 'Blocked')
    )

    role = models.ForeignKey(Hospital_Staff, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    personal_ID_number = models.CharField(max_length=15)
    phone = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    status = models.CharField(max_length=10, choices=STATUS)
    #eployee_ID = models.CharField(max_length=10)
    image = models.ImageField(blank=True, upload_to='images/employees/')
    employed = models.DateTimeField(auto_now_add=True)
    updated_info = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

