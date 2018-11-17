from django.db import models


class new1(models.Model):
    item=models.CharField(max_length=200)
    frequency=models.IntegerField()
class new2(models.Model):
    Date=models.DateField()
    price=models.FloatField(null=False)
