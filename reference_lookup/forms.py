from typing import Any
from django import forms
from taskcode_settings.models import ActivityCodes, FilingFeeCodes, DueCode
from .models import *
from client.models import NatureOfBusiness, Currency
from casefolder.models import FolderType, Status

from django.forms.widgets import NumberInput, TextInput, Textarea, Widget


class IndustryForm(forms.ModelForm):
    class Meta:
        model = NatureOfBusiness
        fields = '__all__'
        widgets = {
            'industry': forms.Textarea(attrs={'class': 'form-control', 'cols': 150, 'rows': 2})
        }

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
        widgets = {
            'currency': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 150, 'rows': 2}),
            'local_rate': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
        }


class AppTypeForm(forms.ModelForm):
    class Meta:
        model = AppType
        fields = '__all__'
        widgets = {
            'apptype': forms.Textarea(attrs={'class': 'form-control', 'cols': 20, 'rows': 1})
        }

class FolderTypeForm(forms.ModelForm):
    class Meta:
        model = FolderType
        fields = '__all__'
        widgets = {
            'folder': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CaseTypeForm(forms.ModelForm):
    class Meta:
        model = CaseType
        fields = '__all__'
        widgets = {
            'case_type': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NatureForm(forms.ModelForm):
    class Meta:
        model = NatureOfCase
        fields = '__all__'
        widgets = {
            'casetype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'nature': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActivityGroupForm(forms.ModelForm):
    class Meta:
        model = ActivityGroup
        fields = '__all__'
        widgets = {
            'case_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'seq' : forms.TextInput(attrs={'class': 'form-control'}),
            'stage_group' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class AppearanceForm(forms.ModelForm):
    class Meta:
        model = Appearance
        fields = '__all__'
        widgets = {
            'appearance': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActivityCodeForm(forms.ModelForm):
    class Meta:
        model = ActivityCodes
        fields = '__all__'
        widgets = {
            'foldertype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'ActivityCode': forms.TextInput(attrs={'class': 'form-control'}),
            'TranType': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'Activity': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'bill_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'amount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'currency': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'pesorate': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'pesoamount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
        }

class DueCodeForm(forms.ModelForm):
    class Meta:
        model = DueCode
        fields = '__all__'
        widgets = {
            'DueCode': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.TextInput(attrs={'class': 'form-control'}),
            'folder_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'apptype' : forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'basisofcompute': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'fieldbsis': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'terms': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
        }

class FilingFeesForm(forms.ModelForm):
    class Meta:
        model = FilingFeeCodes
        fields = 'ActivityCode', 'FeeCode', 'fee_description', 'amount', 'pesoamount'
        widgets = {
            'ActivityCode' : forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'fee_description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
            'pesoamount': NumberInput(attrs={"class": "form-control", "inputmode": "decimal"}),
        }




class CourtsCodeForm(forms.ModelForm):
    class Meta:
        model = Courts
        fields = '__all__'
        widgets = {
            'court': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'presiding_judge': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClGoodsProfileForm(forms.ModelForm):
    class Meta:
        model = ClassOFGoods
        fields = '__all__'
        widgets = {
            'nice_class': forms.TextInput(attrs={'class': 'form-control'}),
            'class_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        widgets = {
            'folder': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }