from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Customer(AbstractUser):
    
    
    BRANCHES = [
        ('Pune', 'Pune'),
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Sangli', 'Sangli'),
    ]
    
    registration_id = models.CharField(max_length=10, unique=True)
    branch = models.CharField(max_length=50,choices=BRANCHES,default='Sangli')
    # //add timezone preference
    timezone = models.CharField(max_length=50,default='Asia/Calcutta')
    
    def __str__(self):
        return self.username