import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Canteen_System_Automation.settings')
import django
django.setup()

import random

from eat_at_canteen.models import FoodItems
from random import randint, choice
import random
int(random.random()*10) / 10.0

from faker import Faker
fakegen=Faker()
def populate(N=5):
    for entry in range(N):

        fake_price=int(random.random()*1000) / 10.0
        fake_name=fakegen.name()
        webpg=FoodItems.objects.get_or_create(Foodname=fake_name,Price=fake_price)[0]
if __name__=='__main__':
    print('ps')
    populate(20)
    print('pc')