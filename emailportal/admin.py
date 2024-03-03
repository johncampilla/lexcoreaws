from django.contrib import admin
from .models import Emails, EmailAttachments

# Register your models here.
admin.site.register(Emails)
admin.site.register(EmailAttachments)
