# Generated by Django 4.0.4 on 2022-06-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuels', '0005_alter_fuel_description_alter_fuel_fuel_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='fuel_status',
            field=models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], default=1, max_length=8, null=True),
        ),
    ]