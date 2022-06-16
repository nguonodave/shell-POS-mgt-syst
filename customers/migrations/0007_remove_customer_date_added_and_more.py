# Generated by Django 4.0.4 on 2022-05-31 07:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_alter_customerstatus_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='customerstatus',
            name='date_added',
        ),
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='customerstatus',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customerstatus'),
        ),
    ]
