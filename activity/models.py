from django.db import models
from matter.models import Matters
from reference_lookup.models import ActivityGroup
from taskcode_settings.models import *
from userprofile.models import *
from casefolder.models import *
# Create your models here.

class task_detail(models.Model):

    TRANTYPE = {
        ('Billable', 'Billable'),
        ('Non-Billable', 'Non-Billable'),
    }

    DOCTYPE = {
        ('Outgoing', 'Outgoing'),
        ('Incoming', 'Incoming'),
        ('Others', 'Others')
    }

    MAILTYPE = {
        ('Email', 'Email'),
        ('Mail', 'Mail'),
        ('Personal', 'Personal'),
        ('IPO', 'IPO'),
        ('Court', 'Court')

    }

    BILLSTATUS = {
        ('Billed', 'Billed'),
        ('Unbilled', 'Unbilled')
    }

    matter = models.ForeignKey(Matters, on_delete=models.CASCADE, null=True)
    tran_date = models.DateField(null=False)
    doc_type = models.CharField(
        max_length=20, choices=DOCTYPE, null=True, blank=True)
    stage_group = models.ForeignKey(ActivityGroup, on_delete=models.CASCADE, blank=True, null=True)
    task_code = models.ForeignKey(
        ActivityCodes, on_delete=models.CASCADE, blank=True, null=True)
    tran_type = models.CharField(
        max_length=15, choices=TRANTYPE, null=True, blank=True)
    lawyer = models.ForeignKey(
        Lawyer_Data, on_delete=models.CASCADE, null=True, blank=True)
    task = models.TextField(null=False, blank=False)
    spentinhrs = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=3)
    spentinmin = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=3)
    doc_date = models.DateField(null=True, blank=True)
    mailing_date = models.DateField(null=True, blank=True)
    examiner = models.CharField(max_length=60, null=True, blank=True)
    mail_type = models.CharField(
        max_length=15, choices=MAILTYPE, null=True, blank=True)
    contact_person = models.CharField(max_length=50, blank=True)
    duecode = models.ForeignKey(
        DueCode, on_delete=models.PROTECT, blank=True, null=True)
    billstatus = models.CharField(
        max_length=15, choices=BILLSTATUS, blank=True, null=True, default='Unbilled')
    createdby = models.CharField(max_length=30, blank=True, null=True)
    updatedby = models.CharField(max_length=30, blank=True, null=True)
    datemodified = models.DateTimeField(auto_now=True)
    datecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.matter.matter_title} - {self.matter.matterno} - { self.tran_date } - {self.task}'

    def save(self, *args, **kwargs):
        if self.doc_type == 'Incoming':
            self.tran_type = 'Non-Billable'
        else:
            self.tran_type = 'Billable'

        super().save(*args, **kwargs)

class FilingDocs(models.Model):
    task_detail = models.ForeignKey(
        task_detail, on_delete=models.CASCADE, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    DocDate = models.DateField(null=True, blank=True)
    DocsPDF = models.FileField(blank=True, null=True, upload_to="Documents/%Y/%m/")
    createdby = models.CharField(max_length=30, blank=True, null=True)
    updatedby = models.CharField(max_length=30, blank=True, null=True)
    datemodified = models.DateTimeField(auto_now=True)
    datecreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Attached Documents'

    def __str__(self):
        return f'{self.DocDate} - {self.DocsPDF}'
    
    @property
    def imageURL(self):
        try:
            img = self.DocsPDF.url
        except:
            img = ""
        return img
