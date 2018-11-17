from django.db import models
from Manager.models import Food_items


# Create your models here.


class Order_Food(models.Model):
    draft = 'dr'
    conf = 'conf'
    status = ((draft, 'draft'), (conf, 'confirmed'),)
    TokenId = models.CharField(max_length=10)
    FoodId = models.ForeignKey(Food_items, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0)
    price = models.FloatField(null=False)
    TableId = models.IntegerField()
    Status = models.CharField(max_length=8, choices=status, default=draft)
    date = models.DateField()
    time = models.TimeField()

class Order_User(models.Model):
    order = 'ordered'
    canc = 'cancelled'
    inPrep = 'in Preparation'
    inDel = 'in Delivery'
    Comp = 'Completed'
    draft = 'draft'
    choice = ((order, 'ordered'), (canc, 'cancelled'), (inPrep, 'in Preparation'), (inDel, 'in Delivery'), (draft, 'draft'), (Comp, 'complete'))
    mailId = models.EmailField(max_length=255, null=False)
    TokenId = models.CharField(max_length=10)
    status = models.CharField(choices=choice, max_length=255, default=draft)
    totalPrice = models.FloatField(null=True)
