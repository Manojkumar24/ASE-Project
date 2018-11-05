from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username


class FoodItems(models.Model):
    Foodname=models.CharField(max_length=150)
    Price=models.FloatField(null=False)

class CustomerFoodItems(models.Model):
    Foodname=models.CharField(max_length=150)
    Price=models.FloatField(default=0.0)
    Quantity=models.IntegerField(null=True)

class Tables(models.Model):
    Table_No=models.IntegerField(null=False)
    Status=models.CharField(null=False,max_length=150)
class Post(models.Model):
    Review = models.TextField()






class Comment(models.Model):
    post = models.ForeignKey('eat_at_canteen.Post', related_name='comments',on_delete='cascade')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("eat_at_canteen:post_list")

    def __str__(self):
        return self.text







