# Generated by Django 2.1.2 on 2018-11-11 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0011_auto_20181112_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
    ]
