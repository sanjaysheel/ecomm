# Generated by Django 3.1b1 on 2020-07-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
