# Generated by Django 3.0.8 on 2020-07-07 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders_address2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
    ]
