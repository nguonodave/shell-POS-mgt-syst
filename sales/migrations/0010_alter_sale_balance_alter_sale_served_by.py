# Generated by Django 4.0.4 on 2022-07-09 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_alter_sale_fuel_alter_sale_served_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='balance',
            field=models.DecimalField(decimal_places=4, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='sale',
            name='served_by',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
