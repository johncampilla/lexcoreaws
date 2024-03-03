from django.db import models
from client.models import Client_Data
from userprofile.models import *

# Create your models here.


class FolderType(models.Model):
    folder = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Folder Type'

    def __str__(self):
        return f'{self.folder}'


class Status(models.Model):
    folder = models.ForeignKey(
        FolderType, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.status}'


class Lawyer_Data(models.Model):
    lawyerID = models.ForeignKey(User_Profile, on_delete=models.PROTECT)
    lawyer_name = models.CharField(max_length=60)
    access_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=100)
    hourlyrate = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    IBPRollNo = models.CharField(max_length=40, blank=True, null=True)
    IBPChapter = models.CharField(max_length=35, blank=True, null=True)
    IBPLifetimeNo = models.CharField(max_length=35, blank=True, null=True)
    Specialization = models.CharField(max_length=150, blank=True, null=True)
#    profile_pic = models.ImageField(blank=True)
    remarks = models.CharField(max_length=200)
    date_hired = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Lawyers'

    def __str__(self):
        return f'{self.access_code}'


class CaseFolder(models.Model):
    client = models.ForeignKey(Client_Data,
                               on_delete=models.CASCADE, null=True)
    folder_description = models.CharField(max_length=200)
    folder_type = models.ForeignKey(FolderType, on_delete=models.CASCADE, null=True)
    Supervisinglawyer = models.ForeignKey(
        Lawyer_Data, on_delete=models.CASCADE, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Case Folders'

    def __str__(self):
        return f'{self.client} - {self.folder_description}'
    
    @property
    def folder_matters(self):
        return self.matters.all()
    
    def get_matters(self):
        return self.matters.all()
