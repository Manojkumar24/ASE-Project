from django import forms
from .models import Food_items, Available_Towns, Dining_Tables


class Add_food(forms.ModelForm):
    class Meta:
        model = Food_items
        fields = '__all__'


class get_id(forms.Form):
    Id = forms.IntegerField()


class Add_tables(forms.Form):
    class Meta:
        model = Dining_Tables
        fields = '__all__'


class Add_city(forms.Form):
    class Meta:
        model = Available_Towns
        fields = '__all__'


class Remove_city(forms.Form):
    town = forms.CharField()
