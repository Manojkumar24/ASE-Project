# Generated by Django 2.1.2 on 2018-12-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
