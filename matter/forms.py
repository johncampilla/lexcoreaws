from typing import Any
from django import forms
from .models import *
from activity.models import task_detail
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class MatterForm(forms.ModelForm):
    class Meta:
        model = Matters
        fields = ('matter_title', 'appearance', 'matter_contact_person', 'handling_lawyer','opposing_counsel', 'apptype', 'clientrefno', 'referenceno', 'filing_date', 'matterno', 'case_type', 'filed_at', 'nature', 'lawyers_involve', 'remarks', 'stage_group')
        required = ('matter_title','handling_lawyer','apptype', 'case_type')
        widgets = {
#            'folder': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'matter_title': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'appearance': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'matter_contact_person': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'handling_lawyer': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'opposing_counsel': forms.TextInput(attrs={'class': 'form-control'}),
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

class EditMatterForm(forms.ModelForm):
    class Meta:
        model = Matters
        fields = 'folder','matter_title', 'appearance', 'matter_contact_person', 'handling_lawyer','opposing_counsel', 'status', 'apptype', 'clientrefno', 'referenceno', 'filing_date', 'matterno', 'case_type', 'filed_at', 'nature', 'lawyers_involve', 'remarks', 'stage_group'
        widgets = {
            'folder': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
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

class PriorityForm(forms.ModelForm):
    class Meta:
        model = ConventionPriority
        fields = 'priority_number','priority_date', 'priority_country_filing', 'certified_copy_attached'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'priority_number': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_country_filing': forms.TextInput(attrs={'class': 'form-control'}),
            'certified_copy_attached': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),

        }
class IP_MatterForm(forms.ModelForm):
    class Meta:
        model = IP_Matter
        fields = '__all__'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'apptype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'status': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'parent_appno': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_appdate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'claim_of_color': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
            'disclaimer': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_mark': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'ipo_examiner': forms.TextInput(attrs={'class': 'form-control'}),
            'application_no': forms.TextInput(attrs={'class': 'form-control'}),
            'application_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'certificate_no': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'ipc_appno': forms.TextInput(attrs={'class': 'form-control'}),
            'ipc_appdate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'publication_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_number': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_country_filing': forms.TextInput(attrs={'class': 'form-control'}),
            'pct_appno': forms.TextInput(attrs={'class': 'form-control'}),
            'pct_appdate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'pct_publication': forms.TextInput(attrs={'class': 'form-control'}),
            'pct_pubdate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'date_Of_PCTPriority': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'lng_interappln': forms.TextInput(attrs={'class': 'form-control'}),
            'lng_interpubln': forms.TextInput(attrs={'class': 'form-control'}),
            'reason_withdrawn': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_Withdrawn': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'copyright_number': forms.TextInput(attrs={'class': 'form-control'}),
            'renewal_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
        }

class Edit_IPTMMatterForm(forms.ModelForm):
    class Meta:
        model = IP_Matter
        fields = 'apptype','ipo_examiner','status','application_no','application_date','certificate_no','registration_date','ipc_appno','ipc_appdate','publication_reference','publication_date','priority_number','priority_date','priority_country_filing','claim_of_color','translation','disclaimer','type_of_mark','reason_withdrawn','date_of_Withdrawn','copyright_number','renewal_date', 'IR_date', 'IR_renewalDate', 'pct_appno', 'pct_appdate', 'pct_publication', 'pct_pubdate', 'lng_interappln', 'lng_interpubln', 'parent_appno', 'parent_appdate'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'apptype': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'status': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'claim_of_color': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
            'disclaimer': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_mark': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'ipo_examiner': forms.TextInput(attrs={'class': 'form-control'}),
            'application_no': forms.TextInput(attrs={'class': 'form-control'}),
            'application_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'certificate_no': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'ipc_appno': forms.TextInput(attrs={'class': 'form-control'}),
            'ipc_appdate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'publication_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_number': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_country_filing': forms.TextInput(attrs={'class': 'form-control'}),
            'reason_withdrawn': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_Withdrawn': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'IR_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'IR_renewalDate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'copyright_number': forms.TextInput(attrs={'class': 'form-control'}),
            'renewal_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'pct_appno' : forms.TextInput(attrs={'class': 'form-control'}),
            'pct_appdate' : NumberInput(attrs={'type': 'date','class':'form-control'}),
            'pct_publication' : forms.TextInput(attrs={'class': 'form-control'}),
            'pct_pubdate' : NumberInput(attrs={'type': 'date','class':'form-control'}),
            'lng_interappln' : forms.TextInput(attrs={'class': 'form-control'}),
            'lng_interpubln' : forms.TextInput(attrs={'class': 'form-control'}),
            'parent_appno' : forms.TextInput(attrs={'class': 'form-control'}),
            'parent_appdate' : NumberInput(attrs={'type': 'date','class':'form-control'}),

        }

            

class DueDateForm(forms.ModelForm):
    class Meta:
        model = AppDueDate
        fields = 'duecode', 'duedate', 'particulars', 'date_complied'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duecode': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duedate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'particulars': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),  
            'date_complied': NumberInput(attrs={'type': 'date','class':'form-control'}),
        }

class NewDueDateForm(forms.ModelForm):
    class Meta:
        model = AppDueDate
        fields = '__all__'
        widgets = {
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duecode': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'duedate': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'particulars': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),  
            'date_complied': NumberInput(attrs={'type': 'date','class':'form-control'}),
        }

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Matter_Applicant
        fields = '__all__' 
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'main_applicant': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'applicant': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),  
        }

class EditApplicantForm(forms.ModelForm):
    class Meta:
        model = Matter_Applicant
        fields = 'main_applicant','applicant','remarks'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'main_applicant': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'applicant': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),  
        }

class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model  =  Applicant
        fields = 'applicant', 'category', 'entity_type', 'position', 'sex', 'first_name', 'middle_name', 'last_name', 'contact_no', 'email', 'nationality', 'applicant_isinventor', 'address', 'city', 'state', 'country', 'zipcode'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'applicant': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'entity_type': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'applicant_isinventor': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InventorForm(forms.ModelForm):
    class Meta:
        model  =  Inventor
        fields = '__all__'
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'city' : forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MatterInventorForm(forms.ModelForm):
    class Meta:
        model  = Matter_Inventor
        fields = '__all__'
        widgets = {
            'inventor': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }

class IPImageForm(forms.ModelForm):
    class Meta:
        model = IP_MatterImage
        fields = '__all__'
        widgets = {
            'matter'  : forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'docdate' : NumberInput(attrs={'type': 'date','class':'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            
        }

class NewCaseDescriptionForm(forms.ModelForm):
    class Meta:
        model = CaseDescription
        fields = 'case_description', 'case_theory', 'submittedby'
        widgets = {
            'case_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  
            'case_theory': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  
            'submittedby': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),

        }

class NewCaseEvidenceForm(forms.ModelForm):
    class Meta:
        model = CaseEvidence
        fields = 'date_submitted', 'source_evidence', 'evidence_description', 'evidence_file'
        widgets = {
            'date_submitted': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'source_evidence': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  
            'evidence_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),  

        }

# class NewProceduralHistoryForm(forms.ModelForm):
#     class Meta:
#         model = CaseHistory
#         fields = 'procedural_history'
#         widgets = {
#             'procedural_history' : forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3})
#         }
class NewPriorityForm(forms.ModelForm):
    class Meta:
        model = ConventionPriority
        fields= 'priority_number', 'priority_date', 'priority_country_filing', 'certified_copy_attached'
        widgets = {
            'priority_number': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_country_filing': forms.TextInput(attrs={'class': 'form-control'}),
            'certified_copy_attached': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 1}),
        }

class EditPriorityForm(forms.ModelForm):
    class Meta:
        model = ConventionPriority
        fields= 'priority_number', 'priority_date', 'priority_country_filing', 'certified_copy_attached'
        widgets = {
            'priority_number': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_date': NumberInput(attrs={'type': 'date','class':'form-control'}),
            'priority_country_filing': forms.TextInput(attrs={'class': 'form-control'}),
            'certified_copy_attached': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 1}),
        }

class ClGoodsForm(forms.ModelForm):
    class Meta:
        model = Matter_ClassOfGoods
        fields= '__all__'
        widgets = {
            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'nice_class': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 1}),
            'class_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),
        }

class EditClGoodsForm(forms.ModelForm):
    class Meta:
        model = Matter_ClassOfGoods
        fields= 'nice_class', 'class_description'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'nice_class': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 1}),
            'class_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 200, 'rows': 3}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = task_detail
        fields = 'tran_date', 'doc_date', 'mailing_date', 'doc_type', 'stage_group','task_code', 'tran_type','lawyer', 'task', 'spentinhrs', 'spentinmin', 'mail_type', 'duecode', 'contact_person', 'billstatus'
        widgets = {
#            'matter': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
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


    