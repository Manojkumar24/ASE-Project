from django.db import models

<<<<<<< HEAD
=======



>>>>>>> 76e5e320e1fa433c0ce48a136d140fe5e264a3bb

class new1(models.Model):
    item=models.CharField(max_length=200)
    frequency=models.IntegerField()
class new2(models.Model):
    Date=models.DateField()
    price=models.FloatField(null=False)
