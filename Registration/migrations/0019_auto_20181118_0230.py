# Generated by Django 2.1.2 on 2018-11-17 21:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0018_auto_20181117_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetails',
            name='employee_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]