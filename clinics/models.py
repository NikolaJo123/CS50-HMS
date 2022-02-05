from turtle import title
from django.db import models


# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    keywords = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name
