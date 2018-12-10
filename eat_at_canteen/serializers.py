from rest_framework import serializers
from .models import Review

class reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=('pub_date','user_name','comment','rating')
    
