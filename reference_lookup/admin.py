from django.contrib import admin
from . models import *
from client.models import Currency



# Register your models here.
admin.site.register(ActivityGroup)
admin.site.register(AppType)
admin.site.register(CaseType)
admin.site.register(NatureOfCase)
admin.site.register(Appearance)
admin.site.register(Courts)
admin.site.register(ClassOFGoods)
admin.site.register(Currency)
