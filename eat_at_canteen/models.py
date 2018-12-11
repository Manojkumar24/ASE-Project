from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
import numpy as np
from datetime import date
from datetime import datetime
from Manager.models import Food_items

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(default=datetime.now)
    user_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)


class user_review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=200)
    latest_review = models.CharField(max_length=200, null=True)
    latest_pub_date = models.DateTimeField(default=datetime.now)
    No_Reviews = models.IntegerField(default=0)
    average_rating = models.FloatField(max_length=10)


class item_review(models.Model):
    product = models.ForeignKey(Food_items, default=None, on_delete=models.CASCADE)
    latest_pub_date = models.DateTimeField(default=datetime.now)
    customer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    rating = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
