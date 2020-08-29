from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class myusers(AbstractUser):

    AHMEDABAD = 'AH'
    SURUT = 'SU'
    VADODRA = 'VA'
    RAJKOT = 'RJ'
    city_of_gujrat = [(AHMEDABAD, 'Ahmedabad'),
                     (SURUT, 'Surat'),
                     (VADODRA, 'Vadodra'),
                     (RAJKOT, 'Rajkot')]
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    )

    company = models.CharField(max_length=20,null=True,blank=True,default=' ')
    phone_number = models.CharField(max_length=10,help_text='enter your 10 digit phone number',null=True,blank=True)
    message = models.TextField(null=True,blank=True,default='')
    city = models.CharField(choices=city_of_gujrat,max_length=25,null=True,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length = 20,default='MALE',null=True,blank=True)

class Accessories(models.Model):
    Brand = models.CharField(max_length=50,verbose_name='Accessories brand')
    Name = models.CharField(max_length=50,verbose_name='name of product')
    Model_number = models.CharField(max_length=50,null=True,blank=True)
    Description = models.TextField(null=True,blank=True)
    price = models.IntegerField()
    Avaible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Mobile(models.Model):
    Brand = models.CharField(max_length=50,verbose_name='Mobile brand')
    Model_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=8,help_text='enter 8 digit serial number')
    Description = models.TextField(null=True,blank=True)
    price = models.IntegerField()
    Avaible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Brand

class products(models.Model):
    accessories = models.ForeignKey(Accessories,on_delete=models.CASCADE)
    mobile = models.ForeignKey(Mobile,on_delete=models.CASCADE)


