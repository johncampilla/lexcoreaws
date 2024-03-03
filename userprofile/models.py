from django.db import models
from django.contrib.auth.models import User

RANK = (
    ('MANAGING PARTNER', 'MANAGING PARTNER'),
    ('PARTNER', 'PARTNER'),
    ('ASSOCIATES', 'ASSOCIATES'),
    ('SECRETARY', 'SECRETARY'),
    ('PARALEGAL', 'PARALEGAL'),
    ('MIS STAFF', 'MIS STAFF'),
    ('SYSTEM ADMIN', 'SYSTEM ADMIN'),
    ('ACCOUNTING STAFF', 'ACCOUNTING STAFF'),
    ('DATA ENCODER', 'DATA ENCODER'),
    ('FRONTEND DEVELOPER', 'FRONTEND DEVELOPER'),
    ('BACKEND DEVELOPER', 'BACKEND DEVELOPER'),
    ('SYSTEM DEVELOPER', 'SYSTEM DEVELOPER'),
    ('CLIENT', 'CLIENT'),

)


class User_Profile(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    rank = models.CharField(max_length=30, choices=RANK, null=True)
    access_code = models.CharField(max_length=5, null=True, blank=True)
    supporto = models.CharField(max_length=60, null=True, blank=True)
    mobile = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to='Profile_Images/', blank=True)
    remarks = models.TextField(null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date_acquired = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return f'{self.userid.username}'

class IP_ResidentAgent(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Femail', 'Female')
    )
    agentnumber = models.CharField(max_length=30, null=True, blank=True)
    companyname = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=30, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    town = models.CharField(max_length=60, blank=True, null=True)
    province = models.CharField(max_length=60, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    contactno = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)

