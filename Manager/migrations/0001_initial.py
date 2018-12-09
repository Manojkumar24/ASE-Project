# Generated by Django 2.1.2 on 2018-11-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Available_Towns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Towns', models.CharField(max_length=225, unique=True)),
                ('pincode', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dining_Tables',
            fields=[
                ('Table_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('availability', models.BooleanField(default=True)),
                ('size', models.IntegerField(default=2)),
                ('zone', models.CharField(choices=[('Normal', 'Normal'), ('Party', 'Party'), ('Family', 'Family')], default='Normal', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Food_items',
            fields=[
                ('Food_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Food_Name', models.CharField(max_length=225)),
                ('Food_Price', models.FloatField()),
                ('Category', models.CharField(max_length=255, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='static/Manager/Foodimg/')),
            ],
        ),
    ]
