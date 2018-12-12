from rest_framework import serializers
from Manager.models import *

class Food_itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food_items
        fields=('Food_id','Food_Name','Food_Price','quantity','Category')
class TownsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Available_Towns
        fields=('Towns','pincode')
class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dining_Tables
        fields=('Table_id','availability','size','zone')
