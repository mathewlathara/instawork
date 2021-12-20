from django.db import models

# Create your models here.

class Employee(models.Model):  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    role_type = models.IntegerField(default=0) # For role_types 0 - regular 1 - admin
    class Meta:
        db_table = 'instaworkapp_employee'