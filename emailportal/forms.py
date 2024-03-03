from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from .models import *

class EmailForm(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email

class NewEmailForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = 'matter', 'subject', 'message', 'email'
        widgets = {
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 5}),
        }

class EmailAttachForm(forms.ModelForm):
    class Meta:
        model = EmailAttachments
        fields = '__all__'
        widgets = {
            'email': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }


    
    