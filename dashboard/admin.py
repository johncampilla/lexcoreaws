from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(NumberOfMattersByAppType)
admin.site.register(NumberOfMattersByLawyers)
admin.site.register(NumberOfMattersByIndustry)
admin.site.register(NumberOfMattersByCaseType)
admin.site.register(NumberOfMattersByFolder)
admin.site.register(NumberOfMattersByNature)
admin.site.register(reportlist)
