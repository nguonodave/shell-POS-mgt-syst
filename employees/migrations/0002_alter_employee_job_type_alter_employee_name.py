# Generated by Django 4.0.4 on 2022-06-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_type',
            field=models.CharField(choices=[('Customer service', 'Customer service'), ('Cashier', 'Cashier')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
