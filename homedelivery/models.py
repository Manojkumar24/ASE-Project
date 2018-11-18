from django.db import models
from Manager.models import Food_items
from django.core.validators import MinValueValidator, RegexValidator
from User.models import Order_Food,Order_User
from django.utils import timezone

# Create your models here.




class HD_Address(models.Model):
    tokenId = models.ForeignKey(Order_User, on_delete=models.CASCADE)
    city_choices = (
        ("Sri City", "Sri City"),
    )
    town = models.CharField(
        max_length=225, choices=city_choices, default='Sri City', null=False)
    street = models.CharField(max_length=225, null=False)
    # dNo : Door number
    dNo = models.CharField(max_length=225, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
