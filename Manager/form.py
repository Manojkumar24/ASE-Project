from django import forms


class Add_food(forms.Form):
    Id = forms.IntegerField()
    Name = forms.CharField()
    Price = forms.FloatField()
    Quantity = forms.IntegerField()
    image = forms.ImageField()
    Category = forms.CharField()


class get_id(forms.Form):
    Id = forms.IntegerField()


class Add_tables(forms.Form):
    Id = forms.IntegerField()
    availability = forms.BooleanField(required=False)
    size = forms.IntegerField()


class Add_city(forms.Form):
    town = forms.CharField()
    pincode = forms.IntegerField()


class Remove_city(forms.Form):
    town = forms.CharField()