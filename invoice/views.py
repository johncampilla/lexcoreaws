from django.shortcuts import render, redirect
from .models import *
from activity.models import task_detail
from client.models import Client_Data
from matter.models import Matter_Applicant, AppType, CaseType
from .forms import *

# Create your views here.
def InvoiceList(request):
    invoice = AccountsReceivable.objects.all().order_by("-bill_date")
    context = {
        'invoices' : invoice,
    }
    return render(request, 'invoice/invoice_list.html', context)

def ViewInvoiceImage(request, pk):

    try:
        invimg = InvoiceImage.objects.get(id = pk)
    except InvoiceImage.DoesNotExist:
        invimg = None
    print(invimg)
    context = {
        'invimg' : invimg, 
    }

    return render(request, 'invoice/invoice_image.html', context)




def ViewInvoice(request, pk):
    invoice = AccountsReceivable.objects.get(id=pk)
    mid = invoice.matter_id
    matter = Matters.objects.get(id = mid)
    activities = task_detail.objects.filter(matter_id = mid)
    applicants = Matter_Applicant.objects.filter(matter__id = mid)
    bills = Bills.objects.filter(ar__id = pk)
    filing_fees = FilingFees.objects.filter(ar__id = pk)
    ope = OPE.objects.filter(ar__id = pk)
    sid = pk
    cid = invoice.matter.folder.client_id
    client = Client_Data.objects.get(id = cid)

    try:
        invimg = InvoiceImage.objects.filter(ar__id = pk)
    except InvoiceImage.DoesNotExist:
        invimg = None



    stype = CaseType.objects.get(id=sid)
    apptype_id = matter.apptype.id
    sapptype = AppType.objects.get(id=apptype_id)

    context = {
        'bills': bills,
        'filing_fees': filing_fees,
        'OPE' : ope,
        'invoice' : invoice,
        'matter': matter,
        'client': client,
        'applicants' : applicants,
        'activities' : activities,
        'invimg' :  invimg
    }

    if sapptype != 'NONIP':
        return render(request, 'invoice/invoice_detail_IP.html', context)
    else :
        return render(request, 'invoice/invoice_detail', context)

def EditInvoice(request, pk):
    pf = AccountsReceivable.objects.get(id=pk)
    bills = Bills.objects.filter(ar__id = pk)
    filing_fees = FilingFees.objects.filter(ar__id = pk)
    sid = pk
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=pf)
        if form.is_valid():
            form.save()
            return redirect('invoice-index')
        else:
            form = InvoiceForm(instance=pf)
    else:
        form = InvoiceForm(instance=pf)

    context = {
        'form': form,
        'bills': bills,
        'filings': filing_fees,
    }
    return render(request, 'invoice/editinvoice.html', context)

def NewInvoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice-index')
        else:
            form = InvoiceForm()
    else:
        form = InvoiceForm()

    context = {
        'form': form,
    }
    return render(request, 'invoice/editinvoice.html', context)

def prepareinvoice(request):
    matters = Matters.objects.all().order_by('-filing_date')

    context = {
        'matters':matters,
    }

    return render(request, 'invoice/allmatters.html', context)

def tobillmatter(request, pk):
    matter = Matters.objects.get(id = pk)
    temppf = TempBills.objects.filter(matter_id = pk)
    tempfees = TempFilingFees.objects.filter(matter_id =pk)
    tempOPE = TempOPE.objects.filter(matter_id = pk)
    invoices = AccountsReceivable.objects.filter(matter_id = pk)
    formPF = TempBillsForm()
    formFees = TempFeesForm()

    
    context = {
        'tempbills' : temppf,
        'tempfees' : tempfees,
        'tempOPE' : tempOPE,
        'matter' : matter,
        'invoices': invoices,
        'formPF' : formPF,
        'formFees':formFees,
    }
    return render(request, 'invoice/matter_invoicedetail.html', context)

def NewTempPf(request):
    if request.method == 'POST':
        form = TempBillsForm(request.POST)
        if form.is_valid():
            tempbill_rec = form.save(commit=False)
            tempbill_rec.matter_id = request.POST['matter']
            tempbill_rec.save()
            return redirect('invoice-matter', request.POST['matter'])

def NewTempFees(request):
    if request.method == 'POST':
        form = TempFeesForm(request.POST)
        if form.is_valid():
            tempfees_rec = form.save(commit=False)
            tempfees_rec.matter_id = request.POST['matter']
            tempfees_rec.save()
            return redirect('invoice-matter', request.POST['matter'])

def EditTempPf(request, pk):
    pf = TempBills.objects.get(id=pk)
    matter = Matters.objects.get(id = pf.matter_id)
    if request.method == 'POST':
        form = TempBillsForm(request.POST, instance=pf)
        if form.is_valid():
            form.save()
            return redirect('invoice-matter', pf.matter_id)
        else:
            form = TempBillsForm(instance=pf)
    else:
        form = TempBillsForm(instance=pf)

    context = {
        'form': form,
        'pf': pf,
        'matter': matter,
    }
    return render(request, 'invoice/invoice_edittemppf.html', context)

def RemoveTempPf(request, pk):
    temppf = TempBills.objects.get(id=pk)
    mid = temppf.matter_id
    temppf.delete()
    return redirect('invoice-matter', mid)

def EditTempFees(request, pk):
    fees = TempFilingFees.objects.get(id=pk)
    matter = Matters.objects.get(id = fees.matter_id)
    if request.method == 'POST':
        form = TempFeesForm(request.POST, instance=fees)
        if form.is_valid():
            form.save()
            return redirect('invoice-matter', fees.matter_id)
        else:
            form = TempFeesForm(instance=fees)
    else:
        form = TempFeesForm(instance=fees)

    context = {
        'form': form,
        'fees': fees,
        'matter': matter,
    }
    return render(request, 'invoice/invoice_edittempfees.html', context)

def RemoveTempfees(request, pk):
    tempfees = TempFilingFees.objects.get(id=pk)
    mid = tempfees.matter_id
    tempfees.delete()
    return redirect('invoice-matter', mid)
