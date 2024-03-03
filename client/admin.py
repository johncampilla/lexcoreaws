from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'address', 'industry','email', 'mobile', 'country', 'date_acquired')
    search_fields = ['client_name', 'address', 'country']
    list_per_page = 10


# Register your models here.
admin.site.register(NatureOfBusiness)
admin.site.register(Client_Data, ClientAdmin)
admin.site.register(Contact_Person)
admin.site.register(Country)
admin.site.register(Client_Bill_Details)
