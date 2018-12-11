from django import forms
from .models import *


class Add_food(forms.ModelForm):
    class Meta:
        model = Food_items
        fields = ['Food_id', 'Food_Name', 'Food_Price', 'Category', 'quantity', 'image']


class get_id(forms.Form):
    Id = forms.IntegerField()


class Add_tables(forms.ModelForm):
    class Meta:
        model = Dining_Tables
        fields = '__all__'


class Add_city(forms.ModelForm):
    class Meta:
        model = Available_Towns
        fields = '__all__'


class Remove_city(forms.Form):
    town = forms.CharField()


class Add_images(forms.ModelForm):
    class Meta:
        model = Admin_Image
        fields = '__all__'


class get_emp_id(forms.Form):
    Employee_id = forms.CharField()