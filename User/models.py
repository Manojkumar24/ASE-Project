from django.db import models
from Manager.models import Food_items
# import datetime

# Create your models here.


class Order_Food(models.Model):
    draft = 'dr'
    conf = 'conf'
    status = ((draft, 'draft'), (conf, 'confirmed'),)
    TokenId = models.CharField(max_length=10)
    FoodId = models.ForeignKey(Food_items,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0)
    price = models.FloatField(null=False)
    date = models.DateField()
    time = models.TimeField()
    TableId = models.IntegerField()
    Status = models.CharField(max_length=8, choices=status, default=draft)


class Order_User(models.Model):
    order = 'ordered'
    canc = 'cancelled'
    inPrep = 'in Preparation'
    inDel = 'in Delivery'
    Comp = 'Completed'
    draf='draft'
    choice = ((order,'ordered'), (canc,'cancelled'), (inPrep,'in Preparation'), (inDel,'in Delivery'), (Comp,'Completed'),(draf,'draft'))
    mailId = models.EmailField(max_length=255, null=False)
    TokenId = models.CharField(max_length=10)
    status = models.CharField(max_length=12, choices=choice, default=draf)
    totalprice=models.FloatField(null=True)
