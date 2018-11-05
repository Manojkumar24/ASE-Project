from django import forms
from eat_at_canteen.models import UserProfileInfo
from django.contrib.auth.models import User
from .models import Post, Comment


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')


'''class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Add_a_Review',)

        widgets = {
            'Add_a_Review': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }'''


