from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from countries.models import Country
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    username = models.CharField(max_length=250, null=True, unique=True)
    contact = models.IntegerField(validators=[MinValueValidator(100000000), MaxValueValidator(999999999)], unique=True, blank=False, default=0)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=False)   
    country = models.ForeignKey(Country, null=True, blank=False, on_delete=models.CASCADE)
    customer_status = models.CharField(max_length=8, null=True, choices=(('1', 'Active'),('0', 'Inactive')), default=1)
    date_created = models.DateTimeField(default=datetime.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

# class CustomerStatus(models.Model):
#     CUSTOMER_STATUS = (
#         ('Active', 'Active'),
#         ('Inactive', 'Inactive'),
#         ('Guest', 'Guest'),
#     )
#     status = models.CharField(max_length=8, choices=CUSTOMER_STATUS)
#     date_created = models.DateTimeField(default=datetime.now)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     def __str__(self):
#         return self.status