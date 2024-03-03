from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import task_detail, FilingDocs
from matter.models import Matters
from reference_lookup.models import CaseType
from taskcode_settings.models import ActivityCodes, FilingFeeCodes
from invoice.models import TempBills, TempFilingFees, TempOPE
from casefolder.models import Lawyer_Data
from .forms import ActivityForm, OutgoingActivityForm, IncomingActivityForm, filingdocforms
from invoice.forms import TempBillsForm, TempFeesForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import string
from django.contrib.auth.decorators import login_required 

@login_required
def DocketingListView(request):
    activities = task_detail.objects.all().order_by('-tran_date')

    context={
        'activities' : activities 
    }

    return render(request, 'activity/index.html', context)

@login_required
def NewActivity(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity_rec = form.save(commit=False)
            activity_rec.matter_id = matter.id
            activity_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            print('invalid ang form pre 1')
            form = ActivityForm()
    else:
        print('invalid ang form pre 2')
        form = ActivityForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'activity/newactivity.html', context)   

@login_required
def EditActivity(request, pk):
    activity = task_detail.objects.get(id=pk)
    mid = activity.matter_id
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('select-activity', activity.id)
        else:
            form = ActivityForm(instance=activity)
    else:
        form = ActivityForm(instance=activity)

    context = {
        'form': form,
        'matter':matter,
        'activity': activity,
    }
    return render(request, 'activity/editactivity.html', context)

@login_required
def ViewActivity(request, pk, mid):
    activity = task_detail.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    docs = FilingDocs.objects.filter(task_detail_id = pk)
    form = ActivityForm(instance=activity)

    context = {
        'form': form,
        'sid': sid,
        'matter': matter,
        'activity': activity,
        'docs' : docs,
    }
    return render(request, 'activity/view_activity.html', context)

@login_required
def viewattachdocument(request, pk):
    docs = FilingDocs.objects.get(id=pk) 
    task = task_detail.objects.get(id = docs.task_detail_id) 
    print(task)
    matter = Matters.objects.get(id = docs.task_detail.matter_id)
    user_name = request.user.username
    print(matter)
    form = filingdocforms(instance=docs)
    if request.method == "POST":
        form = filingdocforms(request.POST, request.FILES, instance=docs)
        if form.is_valid():
            document_rec = form.save(commit=False)
            document_rec.task_detail_id = task.id
            document_rec.updatedby = user_name
            document_rec.save()            
            return redirect('view-activity', task.id, matter.id)
        else:
            form = filingdocforms(instance=docs)
    else:
        form = filingdocforms(instance=docs)

    context = {
        'docs':docs,
        'matter':matter,
        'form' : form,
        'task' : task
    }
    # return render(request, 'matter/viewactivitydocs.html', context)
    return render(request, 'activity/newactivitydocs.html', context)   


@login_required
def RemoveActivity(request, pk):
    activity = task_detail.objects.get(id=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('task-list') 
    
    object = {
        'activity' : activity
    }
    
    return render(request, 'activity/delete.html', object)
    
    return redirect('task-list')

@login_required
def matterlist(request):
    matters = Matters.objects.all().order_by('-filing_date')
    docketlist = task_detail.objects.all().order_by('-tran_date')
    outform = OutgoingActivityForm
    inform = IncomingActivityForm

    context = {
        'matters': matters,
        'docketlist': docketlist,
        'outform': outform,
        'inform': inform,
    }

    return render(request, 'activity/docketlist.html', context)

@login_required
def NewOutgoingActivity(request):
    def createbilableserviceIP():
        bill_description = billcode_rec.bill_description
        bill_amountUSD = billcode_rec.amount
        bill_amountPHP = billcode_rec.pesoamount
        preparedby = lawyer_rec.access_code
        billing = TempBills(
            matter_id = mid, 
            tran_date = request.POST['tran_date'], 
            task_id = sTask_ID,
#            spentinhrs = request.POST['spentinhrs'],
#            spentinmin = request.POST['spentinmin'],
            service_rendered = bill_description,
            USDamount = bill_amountUSD,
            PhPamount = bill_amountPHP,
            recordedby = preparedby,
            status = 'Open',
            )
        billing.save()
        for filing in filingfees:
            fees = TempFilingFees(
                tran_date = request.POST['tran_date'], 
                filing_particulars = filing.fee_description,
                USDamount = filing.amount,
                PhPamount = filing.pesoamount,
                matter_id = mid,
#                service_id = sTask_ID,
                status = "Open",
            )
            fees.save()

    if request.method == 'POST':
        form = OutgoingActivityForm(request.POST)
        if form.is_valid():
            outgoingrec = form.save(commit=False)
            task_code = request.POST['task_code']
            tran_type = request.POST['tran_type']
            tran_date = request.POST['tran_date']
            lawyer_id = request.POST['lawyer']

            mid = request.POST['matter']
            matter = Matters.objects.get(id = mid)

            case_type_id = matter.case_type_id
            case_type = CaseType.objects.get(id = case_type_id)
            
            billcode_rec = ActivityCodes.objects.get(id = task_code)
            lawyer_rec = Lawyer_Data.objects.get(id = lawyer_id)
            filingfees = FilingFeeCodes.objects.filter(ActivityCode_id = task_code)
            outgoingrec.save()
            sTask_ID = outgoingrec.id

            if tran_type == 'Billable' :
                if case_type.case_type == 'IP':
                    createbilableserviceIP()
            
            return redirect('task-list')

@login_required    
def NewIncomingActivity(request):
    if request.method == 'POST':
        form = IncomingActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        
@login_required
def SelectedActivity(request, pk):
    task = task_detail.objects.get(id = pk)
    mid = task.matter_id
    activities = task_detail.objects.filter(matter_id = mid).order_by('-tran_date')
    trandate = task.tran_date
    billables = TempBills.objects.filter(tran_date = trandate, matter_id = mid)
    tempfees = TempFilingFees.objects.filter(tran_date = trandate, matter_id = mid)
    matter = Matters.objects.get(id = mid)

    context = {
        'matter' : matter,
        'task' : task,
        'tempbills' : billables,
        'tempfees' : tempfees,
        'activities' : activities,
    }
    return render(request, 'activity/selected_activitydetail.html', context)

@login_required
def edittempbills(request, pk):
    tempbills = TempBills.objects.get(id=pk)
    task_id = tempbills.task_id
    task = task_detail.objects.get(id=task_id)
    mid = tempbills.matter_id
    matter = Matters.objects.get(id=mid)

    if request.method == 'POST':
        form = TempBillsForm(request.POST, instance=tempbills)
        if form.is_valid():
            form.save()
            return redirect('select-activity', task_id)
        else:
            form = TempBillsForm(instance=tempbills)
    else:
        form = TempBillsForm(instance=tempbills)
    
    context = {
        'form' : form,
        'matter': matter,
        'tempbills': tempbills,
        'task': task,
    }
    return render(request, 'activity/edittempbills.html', context)

@login_required
def edittempfees(request, pk):
    tempfees = TempFilingFees.objects.get(id=pk)
    matter  = Matters.objects.get(id = tempfees.matter_id)

    if request.method == 'POST':
        form = TempFeesForm(request.POST, instance=tempfees)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        else:
            form = TempFeesForm(instance=tempfees)
    else:
        form = TempFeesForm(instance=tempfees)
    
    context = {
        'form' : form,
        'matter': matter,
        'tempfees': tempfees,
    }
    return render(request, 'activity/edittempfees.html', context)

@login_required
def removetembills(request, pk):
    tempbills = TempBills.objects.get(id=pk)
    task_id = tempbills.task_id
    tempbills.delete()
    return redirect('select-activity', task_id)

