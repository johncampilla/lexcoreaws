from django.db import models
from reference_lookup.models import CaseType

# Create your models here.
# Below are the temporary ables for Graphical Visual Data
class NumberOfMattersByAppType(models.Model):
    applicationtype = models.CharField(max_length=20)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.applicationtype} - {self.count}'
class NumberOfMattersByLawyers(models.Model):
    lawyer = models.CharField(max_length=5)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.lawyer} {self.count}"
class NumberOfMattersByIndustry(models.Model):
    industry = models.CharField(max_length=150)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.industry} {self.count}"

class NumberOfMattersByCaseType(models.Model):
    casetype = models.CharField(max_length=60)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.casetype} {self.count}'

class NumberOfMattersByFolder(models.Model):
    folder = models.CharField(max_length=30)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.folder} {self.count}'

class NumberOfMattersByNature(models.Model):
    nature = models.CharField(max_length=100)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nature} {self.count}'
class reportlist(models.Model):
    REPORTGROUP = (
        ('Client','Client'),
        ('Matters','Matters'),
        ('Due Dates', 'Due Dates'),
        ('Invoices', ' Invoices'),
        ('Activities','Activites'),
    )

    casetype = models.ForeignKey(CaseType, on_delete=models.CASCADE)
    reportgroup = models.CharField(max_length=20, choices=REPORTGROUP, null=True, blank=True)
    reportdetail = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.casetype} - {self.reportgroup} - {self.reportdetail}"
    
    class Meta:
        verbose_name_plural = 'Report List'