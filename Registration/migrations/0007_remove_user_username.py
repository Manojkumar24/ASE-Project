# Generated by Django 2.1.2 on 2018-11-11 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0006_auto_20181112_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
