# Generated by Django 4.0.4 on 2022-06-10 10:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuels', '0007_alter_fuel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='price',
            field=models.FloatField(max_length=(15, 2), validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(200)]),
        ),
    ]