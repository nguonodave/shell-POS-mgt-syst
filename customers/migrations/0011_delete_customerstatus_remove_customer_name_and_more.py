# Generated by Django 4.0.4 on 2022-06-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_alter_customer_contact_alter_customer_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerStatus',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='First_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='Last_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_status',
            field=models.CharField(choices=[('1', 'Active'), ('0', 'Inactive'), ('2', 'Guest')], default=1, max_length=8, null=True),
        ),
    ]