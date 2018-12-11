from django.db import models


# Create your models here.

class Food_items(models.Model):
    Food_id = models.IntegerField(null=False, unique=True, primary_key=True)
    Food_Name = models.CharField(max_length=225)
    Food_Price = models.FloatField()
    Category = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='static/Manager/Foodimg/', null=True)
    No_of_reviews = models.IntegerField(default=0)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.Food_Name


dining_table_zone = (('Normal', 'Normal'), ('Party', 'Party'), ('Family', 'Family'))


class Dining_Tables(models.Model):
    Table_id = models.IntegerField(null=False, unique=True, primary_key=True)
    availability = models.BooleanField(default=True)
    size = models.IntegerField(default=2)
    zone = models.CharField(default='Normal', max_length=10, choices=dining_table_zone)

    def __str__(self):
        return str(self.Table_id)


class Available_Towns(models.Model):
    Towns = models.CharField(max_length=225, unique=True)
    pincode = models.IntegerField(null=True)

    def __str__(self):
        return self.Towns


images_choices = (('background', 'background'), ('workplace', 'workplace'), ('service', 'service'))


class Admin_Image(models.Model):
    categories = models.CharField(default='service', max_length=10, choices=images_choices)
    image = models.ImageField(upload_to='static/Manager/Admin_img/', null=True)
