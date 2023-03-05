from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from django.contrib.auth.models import User
from core.models import Location, UserContact
from clinics.models import Department


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


class Speciality(models.Model):
    department = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department


class Employee(Location, UserContact):
    
    class StatusChoice(models.TextChoices):
        ACTIVE = 'Ac', _('Active')
        INACTIVE = 'IA', _('Inactive')
        BLOCKED = 'BL', _('Blocked')

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    role = models.ForeignKey('hospital_staff.Staff', on_delete=models.CASCADE)
    speciality = models.ForeignKey('hospital_staff.Speciality', on_delete=models.CASCADE)
    clinic = models.ForeignKey(Department, on_delete=models.CASCADE)
    personal_ID_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)
    #employee_ID = models.CharField(max_length=10)
    birthdate = models.DateField('birthdate', blank=True, null=True, auto_now=False, auto_now_add=False)
    user_image = models.ImageField(blank=True, upload_to='images/')
    employed = models.DateTimeField(auto_now_add=True)
    updated_info = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    
    def __unicode__(self):
        return u'%s' % (self.department)
    

    def image_tag(self):
        if self.user_image.url is not None:
            return mark_safe('<img src="{}" width="auto" height="50px" />'.format(self.user_image.url))
        else:
            return ""
    
    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True


