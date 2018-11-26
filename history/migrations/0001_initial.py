# Generated by Django 2.1.2 on 2018-10-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FROM', models.DateField()),
                ('TO', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='foodorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('username', models.CharField(max_length=256)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='new1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('frequency', models.IntegerField()),
            ],
        ),
    ]
