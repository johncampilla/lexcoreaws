from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.country}'


class NatureOfBusiness(models.Model):
    industry = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Nature Of Business'

    def __str__(self):
        return f'{self.industry}'


class Currency(models.Model):
    currency = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    local_rate = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Currency'

    def __str__(self):
        return f'{self.currency}'


class Client_Data(models.Model):

    CATEGORIES = (
        ('Corporate', 'Corporate/Company'),
        ('Individual', 'Individual'),
        ('School', 'School'),
        ('Government', 'Government'),
    )
    ENTITYTYPE = (
        ('Big Entity', 'Big Entity'),
        ('Small Entity', 'Small Entity')
    )
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Dormant', 'Dormant'),
        ('Delinquent', ' Delinquent')
    )

    client_number = models.CharField(max_length=30, blank=True, null=True)
    entity_type = models.CharField(max_length=20, choices=ENTITYTYPE, null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, null=True, blank=True)
    client_name = models.CharField(max_length=200)
    unit_description = models.CharField(max_length=50, blank=True, null=True)    
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country_name = models.CharField(max_length=30, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    website = models.CharField(max_length=60, null=True, blank=True )
    zip_code = models.CharField(max_length=30, blank=True)
    landline= models.CharField(max_length=100, blank=True)
    date_acquired = models.DateField(null=True, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    industry = models.ForeignKey(NatureOfBusiness, on_delete=models.CASCADE, null=True)
    date_entered = models.DateField(null=True, blank=True)
    client_type = models.CharField(max_length=1, blank=True, null=True) 
    account_officer = models.CharField(max_length = 50, blank=True, null=True) 
    account_person = models.CharField(max_length = 50, blank=True, null=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default="Active")
    remarks = models.TextField(blank=True, null=True)
    billing_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)
    entered_by = models.CharField(max_length=15, blank=True, null=True)
    referredby = models.CharField(max_length=150, blank=True)
    billing_to = models.CharField(max_length=100, blank=True)
    billing_address = models.CharField(max_length=200, blank=True)
    billing_attention = models.CharField(max_length=60, blank=True)
    billing_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)
    position = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.client_name}'

class Contact_Person(models.Model):
    client = models.ForeignKey(Client_Data, on_delete=models.CASCADE, null=True)
    contact_person = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Client's Contact Persons"

    def __str__(self):
        return f'{self.client} - {self.contact_person}'


class Client_Bill_Details(models.Model):
    client = models.OneToOneField(Client_Data, on_delete=models.CASCADE)
    billing_to = models.CharField(max_length=100, blank=True)
    billing_address = models.CharField(max_length=200, blank=True)
    billing_attention = models.CharField(max_length=60, blank=True)
    billing_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)
    position = models.CharField(max_length=60, blank=True)

    class Meta:
        verbose_name_plural = "Clients Billing Parameters"
    
    def __str__(self):
        return f"{self.billing_to} - {self.billing_currency}"
    

