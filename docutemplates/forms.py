from django import forms
from .models import *

class TemplateForms(forms.ModelForm):
    class Meta:
        model = templatedocs
        fields = 'folder', 'template_name', 'template_docname', 
        widgets = {
            'folder': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'template_name': forms.TextInput(attrs={'class': 'form-control'}),
            'template_docname': forms.TextInput(attrs={'class': 'form-control'}),
        }
