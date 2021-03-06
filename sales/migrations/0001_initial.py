# Generated by Django 4.0.4 on 2022-06-03 20:36

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fuels', '0006_alter_fuel_fuel_status'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('customer_name', models.CharField(max_length=250)),
                ('price', models.FloatField(default=0, max_length=(15, 2), validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(200)])),
                ('volume', models.FloatField(default=0, max_length=(15, 2))),
                ('total_price', models.FloatField(max_length=(15, 2))),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fuels.fuel')),
                ('served_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.employee')),
            ],
        ),
    ]
