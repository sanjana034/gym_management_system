from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.authentication.managers import CustomUserManager

class CustomUser(AbstractUser):
    CLIENT = 'CL'
    FITNESS_INSTRUCTOR = 'FI'
    
    USER_TYPE_CHOICES = [
        (CLIENT, 'Client'),
        (FITNESS_INSTRUCTOR, 'Fitness Instructor'),
    ]
    
    user_id = models.BigAutoField(primary_key=True,)
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default=CLIENT)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=5, blank=True)
    
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.username

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class FitnessInstructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)