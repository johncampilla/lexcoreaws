from django.db import models
from casefolder.models import *
from client.models import Contact_Person
from taskcode_settings.models import DueCode
from reference_lookup.models import *
from django.urls import reverse
# import uuid
# import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from django_countries.fields import CountryField
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# Create your models here.
class Matters(models.Model):
    folder = models.ForeignKey(CaseFolder, on_delete=models.CASCADE, null=True, related_name='matters')
    matter_id = models.CharField(max_length=24, blank=True)
    referenceno = models.CharField(max_length=30, blank=True)
    clientrefno = models.CharField(max_length=60, blank=True)
    matterno = models.CharField(max_length=30, blank=True)
    filing_date = models.DateField(null=True, blank=True)
    filed_at = models.ForeignKey(Courts, on_delete=models.CASCADE, blank=True, null=True)
    case_type = models.ForeignKey(CaseType, on_delete=models.CASCADE, blank=True, null=True)
    apptype = models.ForeignKey(AppType, on_delete=models.CASCADE, blank=True, null=True)
    nature = models.ForeignKey(NatureOfCase, on_delete=models.CASCADE, blank=True, null=True)
    matter_title = models.TextField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    appearance = models.ForeignKey(Appearance, on_delete=models.CASCADE, null=True, blank=True)
    handling_lawyer = models.ForeignKey(Lawyer_Data, on_delete=models.CASCADE, blank=True, null=True)
    matter_contact_person = models.ForeignKey(Contact_Person, on_delete=models.PROTECT, null=True, blank=True)
    lawyers_involve = models.CharField(max_length=60, blank=True, null=True)
    opposing_counsel = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    stage_group = models.ForeignKey(ActivityGroup, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.matter_title} - {self.folder} - {self.matterno}'
    

    class Meta:
        ordering = ('-created_at',)

    class Meta:
        verbose_name_plural = 'Engagements/Accounts'

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
SEX = (
    ('M','Male'),
    ('F','Female'),
)
SEX = (
    ('M','Male'),
    ('F','Female'),
)
YESNO = (
    ('Y','Yes'),
    ('N','No'),
)


class Applicant(models.Model):
    applicant = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    entity_type = models.CharField(max_length=15, choices=ENTITYTYPE, blank=True)
    position = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=10, blank=True, choices=SEX)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    contact_no = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    nationality = models.CharField(max_length=25, blank=True)
    applicant_isinventor= models.CharField(max_length=3, choices=YESNO, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=150, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    zipcode = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = 'Applicants'

    def __str__(self):
        return f"{self.applicant}"

class Matter_Applicant(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, blank=True, null=True)
    remarks = models.TextField(blank=True)
    main_applicant = models.CharField(max_length=10, blank=True, choices=YESNO)

    class Meta:
        verbose_name_plural = 'Matter Applicants'
    
    def __str__(self):
        return f"{self.matter.matter_title} - {self.applicant.applicant}"


class Inventor(models.Model):
    last_name = models.CharField(max_length=60, blank=True)
    first_name = models.CharField(max_length=60, blank=True)
    middle_name = models.CharField(max_length=60, blank=True)
    sex = models.CharField(max_length=10, blank=True, choices=SEX)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=150, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    contact_no = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    nationality = models.CharField(max_length=25, blank=True)

    class Meta:
        verbose_name_plural = 'Inventors/Designers'

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name}'

class Matter_Inventor(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    inventor = models.ForeignKey(Inventor, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Inventors/Designers'

    def __str__(self):
        return f'{self.inventor.last_name}, {self.inventor.first_name} {self.inventor.middle_name}'

class IP_Matter(models.Model):
    STATUS = (
        ('PENDING', 'PENDING'),
        ('REGISTERED', 'REGISTERED'),
        ('CANCELLED', 'CANCELLED'),
        ('ABANDONED', 'ABANDONED'),
        ('RENEWAL', 'RENEWAL'),
        ('TRANSFERRED', 'TRANSFERRED'),
    )
    TYPEOFMARK = (
        ('Word Mark','Word Mark'),
        ('Figurative Mark','Figurative Mark'),
        ('Figurative w/ Word Mark','Figurative w/ Word Mark'),
        ('Three-dimensional','Three-dimensional'),
        ('Collective Mark','Collective Mark'),
    )
    matter = models.OneToOneField(Matters, on_delete=models.CASCADE)
    apptype = models.ForeignKey(AppType, on_delete=models.CASCADE, blank=True, null=True)
    ipo_examiner = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)
    #divisional
    parent_appno = models.CharField(max_length=30, blank=True)
    parent_appdate = models.DateField(null=True, blank=True)
    #local filings
    application_no = models.CharField(max_length=30, blank=True)
    application_date = models.DateField(null=True, blank=True)
    certificate_no = models.CharField(max_length=30, blank=True)
    registration_date = models.DateField(null=True, blank=True)
    ipc_appno = models.CharField(max_length=25, blank=True)
    ipc_appdate = models.DateField(null=True, blank=True)
    publication_reference = models.CharField(max_length=30, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    #applies for all patents
    priority_number = models.CharField(max_length=25, blank=True)
    priority_date = models.DateField(null=True, blank=True)
    priority_country_filing = models.CharField(max_length=30, blank=True)
    #PCT Information
    pct_appno = models.CharField(max_length=30, blank=True)
    pct_appdate = models.DateField(null=True, blank=True)
    pct_publication = models.CharField(max_length=30, blank=True)
    pct_pubdate = models.DateField(null=True, blank=True)
    lng_interappln = models.CharField(max_length=30, blank=True)
    lng_interpubln = models.CharField(max_length=30, blank=True)
    #trademark
    claim_of_color = models.CharField(max_length=30, blank=True)
    translation = models.CharField(max_length=60, blank=True)
    disclaimer = models.CharField(max_length=100, blank=True)
    type_of_mark = models.CharField(max_length=30, blank=True, choices=TYPEOFMARK)
    reason_withdrawn = models.CharField(max_length=200, blank=True)
    date_of_Withdrawn = models.DateField(null=True, blank=True)
    date_Of_PCTPriority = models.DateField(null=True, blank=True)
    copyright_number = models.CharField(max_length=30, blank=True)
    IR_date = models.DateField(null=True, blank=True)
    IR_renewalDate = models.DateField(null=True, blank=True)
    IR_subsequentDate = models.DateField(null=True, blank=True)
    renewal_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Other IP Information'

    def __str__(self):
        return f'{self.matter.matter_title}'

class IP_MatterImage(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="IP_IMAGES/%Y/", blank=True, null=True)
    docdate = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.matter}'
    
    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ""
        return img

class Matter_ClassOfGoods(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    nice_class = models.ForeignKey(ClassOFGoods, on_delete=models.CASCADE, blank=True, null=True)
    class_description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Matters Class Of Goods'

    def __str__(self):
        return f'{self.nice_class} - {self.matter}'

class CPY_Matter(models.Model):
    SUBMISSION = (
        ('Local','Local'),
        ('Foreign','Foreign'),
    )
    REGISTERED = (
        ('IPOPHL','with IPOPHL'),
        ('NLP','with NLP'),
    )

    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    date_of_creation = models.DateField(null=True, blank=True)
    place_of_creation = models.CharField(max_length=100, blank=True)
    classification_of_work = models.TextField(blank=True)
    submission = models.CharField(max_length=10, choices=SUBMISSION, blank=True)
    registered = models.CharField(max_length=5, choices=YESNO, blank=True)
    registered_at = models.CharField(max_length=15, choices=REGISTERED)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'CopyRight Details'

    def __str__(self):
        return f'{self.matter} - {self.date_of_creation}'

class AppDueDate(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    duecode = models.ForeignKey(DueCode, on_delete=models.CASCADE, blank=True, null=True)
    duedate = models.DateField(null=True, blank=True)
    particulars = models.CharField(max_length=250)
    date_complied = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Due Dates'

    def __str__(self):
        return f'{self.matter} - {self.duedate} - {self.particulars}'

class CaseEvidence(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE, null=True, blank=True)
    date_submitted = models.DateField(null=True, blank=True)
    source_evidence = models.TextField(blank=True)
    evidence_description = models.TextField(blank=True)
    evidence_file = models.FileField(blank=True, null=True, upload_to="Evidences/%Y/%m/%D/")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Case Evidences'

class CaseHistory(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE, null=True)
    procedural_history = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Procedural History'
    
    def __str__(self):
        return f'{self.matter}'
            
    
class CaseDescription(models.Model):
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE, null=True)
    case_description = models.TextField(blank=True, null=True)
    case_theory = models.TextField(blank=True, null=True)
    submittedby = models.ForeignKey(Lawyer_Data, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add =True)
    updated = models.DateField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Case Description/Theory'

    def __str__(self):
        return f'{self.matter} - {self.case_description}'

class ConventionPriority(models.Model):
    
    YES_NO = (
        ('Y','YES'),
        ('N','No'),
    )
    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    priority_number = models.CharField(max_length=25, blank=True)
    priority_date = models.DateField(null=True, blank=True)
    priority_country_filing = models.CharField(max_length=30, blank=True)
    certified_copy_attached = models.CharField(max_length=3, choices=YESNO, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Convention Priorities'

    def __str__(self):
        return f'{self.matter} - {self.priority_number} - {self.priority_date}'
