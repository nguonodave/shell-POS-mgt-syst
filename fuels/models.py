from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Fuel(models.Model):
    FUEL_TYPES = (
        ('Shell FuelSave Gasoline(unleaded)', 'Shell FuelSave Gasoline(unleaded)'),
        ('Shell FuelSave Diesel', 'Shell FuelSave Diesel'),
        ('Shell Diesel Extra', 'Shell Diesel Extra'),
        ('Shell V-Power', 'Shell V-Power'),
        ('Shell V-Power NITRO+ Premium Gasoline', 'Shell V-Power NITRO+ Premium Gasoline'),
        ('Shell E15 Regular 88', 'Shell E15 Regular 88'),
        ('Shell ClearFLEX E85', 'Shell ClearFLEX E85'),
    )
    name = models.CharField(max_length=250, choices=FUEL_TYPES, unique=True)
    description = models.TextField(null=True, blank=False)  
    fuel_status = models.CharField(max_length=8, null=True, choices=(('active', 'Active'),('inactive', 'Inactive')), default='active')
    price = models.FloatField(validators=[MinValueValidator(100), MaxValueValidator(200)], max_length=(15,2))      
    date_created = models.DateTimeField(default=datetime.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name    

# class FuelStatus(models.Model):
#     # FUEL_STATUS = (
#     #     ('Active', 'Active'),
#     #     ('Inactive', 'Inactive'),        
#     # )
#     status = models.CharField(max_length=8, choices=(('Active','Active'),('Inactive', 'Inactive')))
#     date_created = models.DateTimeField(default=datetime.now)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     def __str__(self):
#         return self.status
