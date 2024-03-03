from django.db import models
from django.contrib.auth.models import User
from userprofile.models import User_Profile
from matter.models import Matters

class Emails(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE, blank=True, null=True)
    sentby = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length = 500)
    message = models.TextField(blank=True, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add= True, blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject} - {self.created_at}'

class EmailAttachments(models.Model):
    email = models.ForeignKey(Emails, on_delete=models.CASCADE, blank=True, null=True)
    emailattachment = models.FileField(blank=True, null=True, upload_to="EmailAttachments/%Y/%m/")
    created_at = models.DateTimeField(auto_now_add= True, blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True, blank=True, null= True)

    def __str__(self):
        return f'{self.email} - {self.emailattachment}'

