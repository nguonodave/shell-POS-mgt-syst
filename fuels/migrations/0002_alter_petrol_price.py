# Generated by Django 4.0.4 on 2022-05-30 08:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petrol',
            name='price',
            field=models.FloatField(default=1, max_length=(15, 2), validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
