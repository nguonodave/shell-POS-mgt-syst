# Generated by Django 4.0.4 on 2022-06-06 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0012_rename_first_name_customer_first_name_and_more'),
        ('sales', '0003_alter_sale_customer_name_alter_sale_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='customer_name',
            field=models.ForeignKey(default='deleted', null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
    ]