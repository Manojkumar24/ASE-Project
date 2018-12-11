from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea
from .models import Review,item_review
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user_id','pub_date','user_name')
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
class writereview(forms.ModelForm):
    content = forms.CharField(label = "",widget = forms.Textarea(attrs={'class':'form-control','placeholder':'Write about product','rows':'4','cols':'50'}))
    class Meta:
        model = item_review
        fields = ['content']