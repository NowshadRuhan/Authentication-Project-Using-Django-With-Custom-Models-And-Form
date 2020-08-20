from django import forms
from django.contrib.auth.models import User
from Login_app.models import UserInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(label='User Name ',
    help_text ="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
    widget=forms.TextInput(attrs={
    'placeholder':'User Name','style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))
    email = forms.CharField(label='Email ', widget=forms.TextInput(attrs={'type':'email',
    'placeholder':'Enter Email','style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))
    password = forms.CharField(label='Passowrd ', widget=forms.PasswordInput(attrs={ 'type':'password',
    'placeholder':'Enter Passowrd','style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))

    class Meta():
        model = User
        fields = ("username", "email", "password")

class UserInfoForm(forms.ModelForm):
    facebook_id = forms.CharField(label='Facebook Id ', widget=forms.TextInput(attrs={
    'placeholder':'Enter Facebook Id ULR','style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))
    class Meta():
        model = UserInfo
        fields = ('facebook_id', 'profile_pic')
