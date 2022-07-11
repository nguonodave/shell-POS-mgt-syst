# Generated by Django 4.0.4 on 2022-07-09 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_employee_user'),
        ('sales', '0010_alter_sale_balance_alter_sale_served_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='served_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee'),
        ),
    ]
