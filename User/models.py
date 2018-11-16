from django.db import models
# import datetime

# Create your models here.


class Order_Food(models.Model):
    draft = 'dr'
    conf = 'conf'
    status = ((draft, 'draft'), (conf, 'confirmed'),)
    TokenId = models.IntegerField(null=False)
    FoodId = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False, default=0)
    price = models.FloatField(null=False)
    date = models.DateField()
    time = models.TimeField()
    TableId = models.IntegerField()
    Status = models.CharField(max_length=8, choices=status, default=conf)


class Order_User(models.Model):
    order = 'ordered'
    canc = 'cancelled'
    inPrep = 'in Preparation'
    inDel = 'in Delivery'
    Comp = 'Completed'
    choice = ((order,'ordered'), (canc,'cancelled'), (inPrep,'in Preparation'), (inDel,'in Delivery'), (Comp,'Completed'))
    mailId = models.EmailField(max_length=255, null=False)
    TokenId = models.ForeignKey(Order_Food, on_delete=models.PROTECT)
    status = models.CharField(max_length=12, choices=choice, default=order)
