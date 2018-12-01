# Generated by Django 2.1.2 on 2018-12-01 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffdetails',
            fields=[
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=150)),
                ('pincode', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
