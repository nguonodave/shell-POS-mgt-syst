from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class Country(models.Model):
    OPERATING_COUNTRIES = (
        ('Kenya', 'Kenya'),
        ('Nigeria', 'Nigeria'),
        ('Tanzania', 'Tanzania'),
    )
    name = models.CharField(max_length=25, choices=OPERATING_COUNTRIES)        
    date_created = models.DateTimeField(default=datetime.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name