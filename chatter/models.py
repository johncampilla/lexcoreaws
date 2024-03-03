from django.db import models
from userprofile.models import User_Profile
from matter.models import Matters

# Create your models here.
class inboxmessage(models.Model):
    STATUS = {
        ('READ', 'READ'),
        ('UNREAD', 'UNREAD'),
    }
    
    messageto = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    messagefrom = models.CharField(max_length=60, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    messagebox = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, null=True,
                              blank=True, default='UNREAD', choices=STATUS)
    see_matter = models.ForeignKey(
        Matters, on_delete=models.PROTECT, null=True, blank=True)
    updatedby = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sent Messages'

    def __str__(self):
        return f'from {self.messagefrom} to {self.messageto} {self.created_at} - {self.messagebox}'

class tempchatmessages(models.Model):
    STATUS = {
        ('READ', 'READ'),
        ('UNREAD', 'UNREAD'),
    }
    
    messageto = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    messagefrom = models.CharField(max_length=60, null=True, blank=True)
    messagedate = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    messagebox = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, null=True,
                              blank=True, default='UNREAD', choices=STATUS)
    see_matter = models.ForeignKey(
        Matters, on_delete=models.PROTECT, null=True, blank=True)
    updatedby = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Chat Message'

    def __str__(self):
        return f'from {self.messagefrom} to {self.messageto} {self.created_at} - {self.messagebox}'
