# Generated by Django 2.1.1 on 2018-11-16 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eat_at_canteen', '0006_auto_20181105_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='ORDER_FOOD',
            fields=[
                ('TOKENID', models.AutoField(primary_key=True, serialize=False)),
                ('FOODID', models.IntegerField(max_length=15)),
                ('QUANTITY', models.IntegerField()),
                ('PRICE', models.FloatField()),
                ('DATE', models.DateField(default=datetime.date(2018, 11, 16))),
                ('TIME', models.TimeField(default=datetime.datetime(2018, 11, 16, 14, 47, 7, 935688))),
                ('TABLEID', models.IntegerField()),
                ('STATUS2', models.BooleanField(default='draft')),
            ],
        ),
    ]
