from django.db import models
from casefolder.models import FolderType

# Create your models here.
class templatedocs(models.Model):
    folder = models.ForeignKey(FolderType, on_delete=models.CASCADE, null=True)
    template_name = models.CharField(max_length=100, blank=True, null=True)
    template_docname = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.folder} - {self.template_name}'


