# Generated by Django 3.1b1 on 2020-07-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200709_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]