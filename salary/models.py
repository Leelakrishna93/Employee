from django.db import models # type: ignore

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    lhoto=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    email_address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)