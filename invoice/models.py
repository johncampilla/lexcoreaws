from django.db import models
from matter.models import Matters
from activity.models import task_detail
from taskcode_settings.models import ActivityCodes

class TempBills(models.Model):

    BILLSTATUS = (
        ('Open', 'Open'),
        ('Proforma', 'Proforma'),
        ('Billed', 'Billed'),
        ('Cancelled', 'Cancelled'),
        ('Waived', 'Waived'),

    )

    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    task = models.ForeignKey(task_detail, on_delete=models.CASCADE, blank=True, null=True)
    tran_date = models.DateField(null=True, blank=True)
    service_rendered = models.TextField(max_length=250, blank=True)
    spentinhrs = models.IntegerField(null=True, blank=True)
    spentinmin = models.IntegerField(null=True, blank=True)
    USDamount = models.DecimalField(max_digits=10, decimal_places=2)
    PhPamount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=BILLSTATUS, blank=True, default='Open')
    recordedby = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Temporary Billing Services'

    def __str__(self):
        return f'{self.matter.matter_title} - {self.tran_date} {self.task.task}'


class TempFilingFees(models.Model):

    FILINGSTATUS = (
        ('Open', 'Open'),
        ('Proforma', 'Proforma'),
        ('Billed', 'Billed'),
        ('Cancelled', 'Cancelled'),
        ('Waived', 'Waived'),

    )

    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    service = models.ForeignKey(TempBills, on_delete=models.CASCADE, blank=True, null=True)
    tran_date = models.DateField(null=True, blank=True)
    filing_particulars = models.CharField(max_length=250, null=True, blank=True)
    USDamount = models.DecimalField(max_digits=10, decimal_places=2)
    PhPamount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=FILINGSTATUS, blank=True, default='Open')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class TempOPE(models.Model):

    FILINGSTATUS = (
        ('Open', 'Open'),
        ('Billed', 'Billed'),
        ('Cancelled', 'Cancelled'),
        ('Waived', 'Waived'),

    )

    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    service = models.ForeignKey(TempBills, on_delete=models.CASCADE, blank=True, null=True)
    tran_date = models.DateField(null=True, blank=True)
    expnse_particulars = models.CharField(max_length=250, null=True, blank=True)
    USDamount = models.DecimalField(max_digits=10, decimal_places=2)
    PhPamount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=FILINGSTATUS, blank=True, default='Open')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class AccountsReceivable(models.Model):

    PAYMENTTAG = (
        ('UN', 'Unpaid'),
        ('CN', 'Cancelled'),
        ('PP', 'Partially Paid'),
        ('WV', 'Waived'),
        ('CN', 'Cancelled'),
        ('WO', 'Write-Off'),
    )

    matter = models.ForeignKey(Matters, on_delete=models.CASCADE)
    bill_no = models.CharField(max_length=15, blank=True)
    bill_date = models.DateField(blank=True, null=True)
    total_USDamount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    total_PhPamount= models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    pf_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    filing_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ope_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    peso_rate_used = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    payment_tag = models.CharField(max_length=15, choices=PAYMENTTAG, blank=True, default='UN')

    def __str__(self):
        return f'{self.bill_no} {self.matter.matter_title}'

class Bills(models.Model):
    ar = models.ForeignKey(AccountsReceivable, on_delete=models.CASCADE)
    task = models.ForeignKey(task_detail, on_delete=models.CASCADE, blank=True, null=True) 
    taskcode = models.CharField(max_length=15, blank=True, null=True)
    service_rendered = models.TextField(blank=True)
    lawyer_name = models.CharField(max_length=60, blank=True, null=True)
    hourlyrate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    spentinhrs = models.IntegerField(null=True, blank=True)
    spentinmin = models.IntegerField(null=True, blank=True)
    pf_USDamount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    pf_PhPamount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.ar} - {self.service_rendered}'

class InvoiceImage(models.Model):
    ar = models.ForeignKey(AccountsReceivable, on_delete=models.CASCADE)
    invoiceImage = models.ImageField(upload_to="invoices/%Y/", blank=True, null=True)

    def __str__(self):
        return f'{self.ar} - {self.invoiceImage}'


class FilingFees(models.Model):
    ar = models.ForeignKey(AccountsReceivable, on_delete=models.CASCADE)
    pfdetail = models.ForeignKey(Bills, on_delete=models.CASCADE)
    filing_particulars = models.TextField(blank=True)
    filing_fee_USDamount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    filing_fee_PHPamount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) 

    def __str__(self):
        return f'{self.ar.bill_no} - {self.filing_particulars}'

class OPE(models.Model):
    ar = models.ForeignKey(AccountsReceivable, on_delete=models.CASCADE)
    task = models.ForeignKey(task_detail, on_delete=models.CASCADE, blank=True, null=True) 
    exp_date = models.DateField(blank=True, null=True)
    exp_code = models.CharField(max_length=10, blank=True, null=True)
    exp_particulars = models.TextField(blank=True)
    exp_USDAmount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    exp_PHPAmount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.ar.bill_no} - {self.exp_particulars}'

# class BookTitle(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(blank=True)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.title}'

#     @property
#     def books(self):
#         return self.book_set.all()

#    def get_books(self):
#        return self.books.all()
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

# class Book(models.Model):
#     title = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
#     isbn = models.CharField(max_length=24, blank=True)
#     qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.title)
    
#     def save(self, *args, **kwargs):
#         if not self.isbn:
#             self.isbn = str(uuid.uuid4()).replace("-", "")[:24].lower()

#             #generate QRCode

#             qrcode_img = qrcode.make(self.isbn)
#             canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
#             canvas.paste(qrcode_img)
#             fname = f'qr_code-{self.title}.png'
#             buffer = BytesIO()
#             canvas.save(buffer, 'PNG')
#             self.qr_code.save(fname, File(buffer), save=False)
#             canvas.close()

#         super().save(*args, **kwargs)
