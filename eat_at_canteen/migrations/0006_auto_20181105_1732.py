# Generated by Django 2.0.7 on 2018-11-05 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_at_canteen', '0005_auto_20181103_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='CustomerFoodItems',
        ),
        migrations.DeleteModel(
            name='FoodItems',
        ),
        migrations.DeleteModel(
            name='Tables',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
