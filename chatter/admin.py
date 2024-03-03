from django.contrib import admin
from .models import inboxmessage, tempchatmessages

# Register your models here.
admin.site.register(inboxmessage)
admin.site.register(tempchatmessages)
