# Generated by Django 4.0.4 on 2022-05-31 07:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fuels', '0003_rename_petrol_fuel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelStatus',
            fields=[
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=8)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='fuel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='name',
            field=models.CharField(choices=[('Shell FuelSave Gasoline(unleaded)', 'Shell FuelSave Gasoline(unleaded)'), ('Shell FuelSave Diesel', 'Shell FuelSave Diesel'), ('Shell Diesel Extra', 'Shell Diesel Extra'), ('Shell V-Power', 'Shell V-Power'), ('Shell V-Power NITRO+ Premium Gasoline', 'Shell V-Power NITRO+ Premium Gasoline'), ('Shell E15 Regular 88', 'Shell E15 Regular 88'), ('Shell ClearFLEX E85', 'Shell ClearFLEX E85')], max_length=250),
        ),
        migrations.AddField(
            model_name='fuel',
            name='fuel_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='fuels.fuelstatus'),
        ),
    ]
