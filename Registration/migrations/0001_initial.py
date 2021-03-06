# Generated by Django 2.1.2 on 2018-12-12 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=225)),
                ('username', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50, null=True)),
                ('canteen_name', models.CharField(max_length=200, null=True)),
                ('canteen_street', models.CharField(max_length=200, null=True)),
                ('canteen_city', models.CharField(max_length=200, null=True)),
                ('canteen_pincode', models.CharField(max_length=6, null=True)),
                ('admin_id', models.CharField(default='ADMN001', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Staffdetails',
            fields=[
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=150)),
                ('pincode', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=100)),
                ('pincode', models.CharField(default='', max_length=6)),
                ('profile_pic', models.ImageField(blank=True, upload_to='static/registration/profile_pics')),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
