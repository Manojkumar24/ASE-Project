# Generated by Django 2.1.2 on 2018-12-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_auto_20181212_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetails',
            name='password',
            field=models.CharField(max_length=400),
        ),
    ]