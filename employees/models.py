import email
import imp
from multiprocessing.spawn import import_main_path
from re import S
from tkinter import E
from unicodedata import name
from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from countries.models import Country
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    JOBS =(
        ('Customer service', 'Customer service'),
        ('Cashier', 'Cashier'),
    )
    user = models.OneToOneField(User, null=True, blank=False, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField(validators=[MinValueValidator(100000000), MaxValueValidator(999999999)], unique=True, blank=False, default=0)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=False)   
    country = models.ForeignKey(Country, null=True, blank=False, on_delete=models.CASCADE) 
    job_type = models.CharField(max_length=20, choices=JOBS)   
    date_created = models.DateTimeField(default=datetime.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)   



