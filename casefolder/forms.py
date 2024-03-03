from typing import Any
from django import forms
from .models import CaseFolder
from matter.models import Matters
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class CaseFolderForm(forms.ModelForm):
    class Meta:
        model = CaseFolder
        fields = 'folder_description', 'folder_type', 'Supervisinglawyer', 'remarks'
        widgets = {
            'folder_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),            
            'folder_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'Supervisinglawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }
class NewCaseFolderForm(forms.ModelForm):
    class Meta:
        model = CaseFolder
        fields = 'client', 'folder_description', 'folder_type', 'Supervisinglawyer', 'remarks'
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'folder_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),            
            'folder_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'Supervisinglawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }


class MatterForm(forms.ModelForm):
    class Meta:
        model = Matters
        fields = ('matter_title', 'appearance', 'matter_contact_person', 'handling_lawyer','opposing_counsel', 'status', 'apptype', 'clientrefno', 'referenceno', 'filing_date', 'matterno', 'case_type', 'filed_at', 'nature', 'lawyers_involve', 'remarks', 'stage_group')
        required = ('matter_title','handling_lawyer','apptype', 'case_type')
        widgets = {
#            'folder': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
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
            'stage_group': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }
