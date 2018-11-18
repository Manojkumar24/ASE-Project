# Generated by Django 2.1.2 on 2018-11-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20181117_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_user',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order_user',
            name='status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('cancelled', 'cancelled'), ('in Preparation', 'in Preparation'), ('in Delivery', 'in Delivery'), ('draft', 'draft'), ('Completed', 'complete')], default='draft', max_length=255),
        ),
        migrations.AlterField(
            model_name='order_user',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
