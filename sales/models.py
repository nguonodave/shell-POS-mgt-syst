from pickle import TRUE
from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from fuels.models import Fuel
from employees.models import Employee
from customers.models import Customer

# Create your models here.
class Sale(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(validators=[MinValueValidator(100), MaxValueValidator(200)], max_length=(15,2))
    volume = models.DecimalField(max_digits=8, decimal_places=4)
    total_price = models.FloatField(max_length=(15,2))
    amount_paid = models.IntegerField(null=True, blank=False)
    balance = models.DecimalField(validators=[MinValueValidator(0)], max_digits=20, decimal_places=4, null=True, blank=False)
    served_by = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.customer_name} - {self.fuel} - {self.volume} L"
