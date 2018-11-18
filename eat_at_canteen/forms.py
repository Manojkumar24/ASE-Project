from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea
from .models import Review
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user_id','pub_date','user_name')
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }