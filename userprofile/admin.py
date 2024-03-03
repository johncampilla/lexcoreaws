from django.contrib import admin
from . models import *
from casefolder.models import Lawyer_Data

# Register your models here.
admin.site.register(User_Profile)
admin.site.register(Lawyer_Data)
