from django.db import models
#mport tornado.platform.twisted
from Manager.models import Food_items
import datetime

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
    date = models.DateField(null=True)
    time = models.TimeField(null=True)


class Order_User(models.Model):
    order = 'ordered'
    cancel = 'cancelled'
    inPrep = 'in Preparation'
    inDel = 'in Delivery'
    user_conf = 'User Conform'
    Comp = 'Completed'
    draft = 'draft'
    choice = ((order, 'ordered'), (cancel, 'cancelled'), (inPrep, 'in Preparation'), (inDel, 'in Delivery'), (draft, 'draft'), (Comp, 'complete'), (user_conf, 'User Conform'))
    mailId = models.EmailField(max_length=255, null=False)
    TokenId = models.CharField(max_length=10)
    status = models.CharField(choices=choice, max_length=255, default=draft)
    totalPrice = models.FloatField(null=True)
