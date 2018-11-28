# Generated by Django 2.1.2 on 2018-11-28 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TokenId', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('TableId', models.IntegerField()),
                ('Status', models.CharField(choices=[('dr', 'draft'), ('conf', 'confirmed')], default='dr', max_length=8)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('FoodId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Food_items')),
            ],
        ),
        migrations.CreateModel(
            name='Order_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailId', models.EmailField(max_length=255)),
                ('TokenId', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('cancelled', 'cancelled'), ('in Preparation', 'in Preparation'), ('in Delivery', 'in Delivery'), ('draft', 'draft'), ('Completed', 'complete')], default='draft', max_length=255)),
                ('totalPrice', models.FloatField(null=True)),
            ],
        ),
    ]
