from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, NumberInput, TextInput, Textarea, Widget
from casefolder.models import Lawyer_Data

from .models import User_Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class UserForm(forms.ModelForm):
    class Meta : 
        model = User_Profile
        fields = 'userid', 'address','rank','access_code','supporto','mobile','remarks','name','date_acquired', 'image'
        widgets = {
            'userid': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'rank': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'access_code': forms.TextInput(attrs={'class': 'form-control'}),
            'supporto' : forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'image' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_acquired': NumberInput(attrs={'type': 'date','class':'form-control'}),
        }    

class EditUserProfileForm(forms.ModelForm):
    class Meta : 
        model = User_Profile
        fields = 'address','rank','access_code','supporto','mobile','remarks','name','date_acquired', 'image'
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'rank': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'access_code': forms.TextInput(attrs={'class': 'form-control'}),
            'supporto' : forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'image' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_acquired': NumberInput(attrs={'type': 'date','class':'form-control'}),
        }    


class LawyerDataForm(forms.ModelForm):
    class Meta:
        model = Lawyer_Data
        fields = 'lawyerID','lawyer_name','access_code','phone','IBPRollNo','IBPChapter','IBPLifetimeNo','Specialization','remarks', 'date_hired'
        Widgets = {
            'lawyerID' : forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'lawyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'access_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'IBPRollNo' : forms.TextInput(attrs={'class': 'form-control'}),
            'IBPChapter' : forms.TextInput(attrs={'class': 'form-control'}),
            'IBPLifetimeNo' : forms.TextInput(attrs={'class': 'form-control'}),
            'Specialization' :  forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),
            'date_hired':NumberInput(attrs={'type': 'date','class':'form-control'}),
        }



# different Login =======================
class userloginform(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class OTPForm(forms.Form):
    otp = forms.CharField(label="OTP", max_length=6)
        