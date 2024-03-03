from typing import Any
from django import forms
from .models import task_detail, FilingDocs
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class OutgoingActivityForm(forms.ModelForm):
    class Meta:
        model=task_detail
        fields='matter', 'tran_date','doc_date', 'stage_group', 'task_code', 'tran_type', 'lawyer', 'task', 'spentinhrs', 'spentinmin', 'mail_type', 'duecode'
        widgets = {
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'tran_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'doc_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'stage_group' : forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'task_code' : forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'tran_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'lawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'task': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'spentinhrs': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'spentinmin': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'mail_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duecode': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2})
        }

class IncomingActivityForm(forms.ModelForm):
    class Meta:
        model=task_detail
        fields='matter', 'tran_date','doc_date', 'mailing_date', 'task_code', 'tran_type', 'contact_person','task', 'mail_type', 'duecode', 'examiner'
        widgets = {
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'tran_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'doc_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'mailing_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'task_code' : forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'tran_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'task': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'mail_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duecode': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'contact_person':forms.TextInput(attrs={'class': 'form-control'}),
            'examiner': forms.TextInput(attrs={'class': 'form-control'}),



        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = task_detail
        fields = 'tran_date', 'doc_date', 'mailing_date', 'doc_type', 'stage_group','task_code', 'tran_type','lawyer', 'task', 'spentinhrs', 'spentinmin', 'mail_type', 'duecode', 'contact_person', 'billstatus'
        widgets = {
            'tran_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'doc_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'mailing_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'doc_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'stage_group': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'task_code': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'tran_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'lawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'task': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'spentinhrs': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'spentinmin': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'examiner': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duecode': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'contact_person' : forms.TextInput(attrs={'class': 'form-control'}),
            'billstatus': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2})
        }
    
class filingdocforms(forms.ModelForm):
    class Meta:
        model = FilingDocs
        fields = '__all__'
        widgets = {
           'Description' : forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}), 
           'DocDate' : NumberInput(attrs={'type': 'date','class':'form-control'}),

        }

class DocumentEditForm(forms.ModelForm):
    class Meta:
        model = FilingDocs
        fields = '__all__'
        widgets = {
            'DocDate': NumberInput(attrs={'type': 'date'}),
        }


