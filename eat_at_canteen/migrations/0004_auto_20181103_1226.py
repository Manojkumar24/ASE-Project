# Generated by Django 2.0.7 on 2018-11-03 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_at_canteen', '0003_auto_20181103_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
