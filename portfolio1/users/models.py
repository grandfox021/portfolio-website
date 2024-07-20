from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class CustomUser(AbstractUser) :
    
    phone_number = PhoneNumberField()
    is_customer = models.BooleanField(default=True)
    profile_pic = models.ImageField(null=True,blank=True,default="maintemplate_images/default_profile_pic.jpg")

