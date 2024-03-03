from django import forms
from . models import inboxmessage


class chatform(forms.ModelForm):
    class Meta:
        model = inboxmessage
        fields = 'messageto', 'subject', 'messagebox', 'status', 'see_matter'
        widgets = {
            'messageto': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'see_matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'messagebox': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }

