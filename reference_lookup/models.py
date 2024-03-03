from django.db import models
from casefolder.models import FolderType


class TaskGroup(models.Model):
    folder = models.ForeignKey(
        FolderType, on_delete=models.PROTECT, null=True, blank=True)
    order_seq = models.IntegerField(null=True, blank=True)
    Stages = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Activity Group'

        def __str__(self):
            return f'{self.folder}'


class AppType(models.Model):
    apptype = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Types Of IP Applications'

    def __str__(self):
        return f'{self.apptype}'


class CaseType(models.Model):
    case_type = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Case Type'

    def __str__(self):
        return f'{self.case_type}'
    
    def get_matters(self):
        self.cases.all()


class NatureOfCase(models.Model):
    casetype = models.ForeignKey(
        CaseType, on_delete=models.PROTECT, null=True, blank=True)
    nature = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Natures Of Cases'

    def __str__(self):
        return f'{self.nature}'


class Appearance(models.Model):
    appearance = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name_plural = 'Appearance'

    def __str__(self):
        return f'{self.appearance}'


class Courts(models.Model):
    court = models.CharField(max_length=60)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=150, blank=True, null=True)
    contact_number = models.CharField(max_length=100, blank=True, null=True)
    presiding_judge = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Courts"

    def __str__(self):
        return f'{self.court}'
    
class ClassOFGoods(models.Model):
    nice_class = models.PositiveSmallIntegerField()
    class_description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Nice Classification Of Goods'

    def __str__(self):
        return f'{self.nice_class}'

class ActivityGroup(models.Model):
    case_type = models.ForeignKey(CaseType, on_delete=models.CASCADE, blank=True, null=True)
    stage_group = models.CharField(max_length=30, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Stage Group"
    
    def __str__(self):
        return f'{self.stage_group}'

