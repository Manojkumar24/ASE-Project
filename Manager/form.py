from django import forms
from django.core.validators import FileExtensionValidator


class Add_food(forms.Form):
    Id = forms.IntegerField()
    Name = forms.CharField()
    Price = forms.FloatField()
    Quantity = forms.IntegerField()
    image = forms.FileField(allow_empty_file=True,
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    Category = forms.CharField()


class get_id(forms.Form):
    Id = forms.IntegerField()


class Add_tables(forms.Form):
    Choices = (('Normal', 'Normal'), ('Party', 'Party'), ('Family', 'Family'))
    Id = forms.IntegerField()
    availability = forms.BooleanField(required=False)
    size = forms.IntegerField()
    zone = forms.ChoiceField(choices=Choices)


class Add_city(forms.Form):
    town = forms.CharField()
    pincode = forms.IntegerField()


class Remove_city(forms.Form):
    town = forms.CharField()
