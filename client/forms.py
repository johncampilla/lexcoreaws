from typing import Any
from django import forms
from .models import *
from casefolder.models import CaseFolder
from activity.models import task_detail
from matter.models import Matters
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client_Data
        fields = '__all__'
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'category': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'entity_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'landline': forms.TextInput(attrs={'class': 'form-control'}),
            'referredby': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'date_acquired': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'billing_to': forms.TextInput(attrs={'class': 'form-control'}),
            'billing_attention': forms.TextInput(attrs={'class': 'form-control'}),
            'billing_address': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'billing_currency': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }


class NewFolderForm(forms.ModelForm):
    class Meta:
        model = CaseFolder
        fields = 'folder_description', 'folder_type', 'Supervisinglawyer', 'remarks'
        widgets = {
#            'client': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'folder_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),            
            'folder_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'Supervisinglawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }
class BillingAdresseeForm(forms.ModelForm):
    class Meta:
        model = Client_Bill_Details   
        fields = '__all__'  
        Widgets = {
            'billing_to': forms.TextInput(attrs={'class': 'form-control'}),
            'billing_address': forms.TextInput(attrs={'class': 'form-control'}),
            'billing_attention': forms.TextInput(attrs={'class': 'form-control'}),
            'billing_currency': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
        } 

class ClientContactsForm(forms.ModelForm):
    class Meta:
        model = Contact_Person
        fields = 'client', 'contact_person', 'position', 'address', 'phone', 'email'
        #fields = '__all__'
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),


        }

class ClientMatterForm(forms.ModelForm):
    class Meta:
        model = Matters
        fields = 'matter_title', 'appearance', 'matter_contact_person', 'handling_lawyer','opposing_counsel', 'status', 'apptype', 'clientrefno', 'referenceno', 'filing_date', 'matterno', 'case_type', 'filed_at', 'nature', 'lawyers_involve', 'remarks'
        widgets = {
            'matter_title': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'appearance': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'matter_contact_person': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'handling_lawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'opposing_counsel': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'apptype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'clientrefno': forms.TextInput(attrs={'class': 'form-control'}),
            'referenceno': forms.TextInput(attrs={'class': 'form-control'}),
            'filing_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'matterno': forms.TextInput(attrs={'class': 'form-control'}),
            'case_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'filed_at': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'nature': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'lawyers_involve': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),

        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = task_detail
        fields = 'matter', 'tran_date', 'doc_date', 'mailing_date', 'doc_type', 'stage_group','task_code', 'tran_type','lawyer', 'task', 'spentinhrs', 'spentinmin', 'mail_type', 'duecode', 'contact_person', 'billstatus'
        widgets = { 
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
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
            'billstatus': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2})
        }
