from django.shortcuts import render, redirect
from . models import *
from .forms import *
from taskcode_settings.models import ActivityCodes, FilingFeeCodes, DueCode
from client.models import *
from casefolder.models import Status
from matter.models import Matters

# Create your views here.

def index(request):
    apptype = AppType.objects.all().order_by('apptype')
    industry = NatureOfBusiness.objects.all().order_by('industry')
    currency = Currency.objects.all()
    folder = FolderType.objects.all().order_by('folder')
    nature = NatureOfCase.objects.all().order_by('casetype', 'nature')
    casetype = CaseType.objects.all().order_by('case_type')
    appearance = Appearance.objects.all().order_by('appearance')
    courts = Courts.objects.all().order_by('court')
    taskcodes = ActivityCodes.objects.all().order_by('foldertype', 'ActivityCode')
    duecodes = DueCode.objects.all().order_by('folder_type', 'DueCode')
    activitygroup = ActivityGroup.objects.all().order_by('-case_type', 'seq')
    status = Status.objects.all().order_by('folder')
    print(status)
    formindustry = IndustryForm()
    formapptype = AppTypeForm()


    context = {
        'apptype': apptype,
        'industry': industry,
        'currency': currency,
        'folder': folder,
        'nature': nature,
        'casetype': casetype,
        'appearance': appearance,
        'courts': courts,
        'taskcodes' : taskcodes,
        'formindustry' : formindustry,
        'formapptype': formapptype,
        'duecodes' : duecodes,
        'activitygroup' : activitygroup,
        'status':status,
    }
    return render(request, 'reference_lookup/index.html', context)

def newIndustryCode(request):
    if request.method == "POST":
        form = IndustryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-industry')
    else:
        form = IndustryForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newindustry.html', context)

def CaseStatus(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-industry')
    else:
        form = StatusForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newstatus.html', context)

def RemoveCaseStatus(request, pk):
    status = Status.objects.get(id=pk) 
    status.delete()
    return redirect('reference-index')

def EditCaseStatus(request, pk):
    status = Status.objects.get(id=pk)
    matters = Matters.objects.filter(status_id = pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = StatusForm(instance=status)
    else:
        form = StatusForm(instance=status)

    context = {
        'form': form,
        'matters':matters,
    }
    return render(request, 'reference_lookup/newstatus.html', context)    

def NewCurrencyCode(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('newcurrency')
    else:
        form = CurrencyForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newcurrency.html', context)


def EditIndustryCode(request, pk):
    industry = NatureOfBusiness.objects.get(id=pk)
    clients = Client_Data.objects.filter(industry_id = pk)
    sid = pk
    if request.method == 'POST':
        form = IndustryForm(request.POST, instance=industry)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = IndustryForm(instance=industry)
    else:
        form = IndustryForm(instance=industry)

    context = {
        'form': form,
        'sid': sid,
        'clients':clients,
    }
    return render(request, 'reference_lookup/newindustry.html', context)

def EditCurrencyCode(request, pk):
    currency = Currency.objects.get(id=pk)
    clients = Client_Data.objects.filter(billing_currency_id = pk)
    sid = pk
    if request.method == 'POST':
        form = CurrencyForm(request.POST, instance=currency)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = CurrencyForm(instance=currency)
    else:
        form = CurrencyForm(instance=currency)

    context = {
        'form': form,
        'sid': sid,
        'clients':clients,
    }
    return render(request, 'reference_lookup/newcurrency.html', context)

def RemoveCurrencyCode(request, pk):
    currency = Currency.objects.get(id=pk) 
    currency.delete()
    return redirect('reference-index')

def RemoveIndustryCode(request, pk):
    industry = NatureOfBusiness.objects.get(id = pk)
    industry.delete()
    return redirect('reference-index')

def NewAppType(request):
    if request.method == "POST":
        form = AppTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-industry')
    else:
        form = AppTypeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newapptype.html', context)

def EditAppType(request, pk):
    apptype = AppType.objects.get(id=pk)
    matters = Matters.objects.filter(apptype_id = pk).order_by('-modified_at')
    sid = pk
    if request.method == 'POST':
        form = AppTypeForm(request.POST, instance=apptype)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = AppTypeForm(instance=apptype)
    else:
        form = AppTypeForm(instance=apptype)

    context = {
        'form': form,
        'sid': sid,
        'matters':matters,
    }
    return render(request, 'reference_lookup/newapptype.html', context)

def RemoveAppType(request, pk):
    apptype = AppType.objects.get(id=pk)
    apptype.delete()
    return redirect('reference-index')

def NewFolderType(request):
    if request.method == "POST":
        form = FolderTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-foldertype')
    else:
        form = FolderTypeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newfoldertype.html', context)

def EditFolderType(request, pk):
    folder = FolderType.objects.get(id=pk)
    matters = Matters.objects.filter(folder__folder_type_id = pk)

    sid = pk
    if request.method == 'POST':
        form = FolderTypeForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = FolderTypeForm(instance=folder)
    else:
        form = FolderTypeForm(instance=folder)

    context = {
        'form': form,
        'sid': sid,
        'matters':matters,
    }
    return render(request, 'reference_lookup/newfoldertype.html', context)
def RemoveFolderType(request, pk):
    folder = FolderType.objects.get(id = pk)
    folder.delete()
    return redirect('reference-index')

def NewCaseType(request):
    if request.method == "POST":
        form = CaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-casetype')
    else:
        form = CaseTypeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newCaseType.html', context)

def EditCaseType(request, pk):
    casetype = CaseType.objects.get(id=pk)
    matters = Matters.objects.filter(case_type_id = pk).order_by('-modified_at')
    #matters = casetype.get_matters()
    sid = pk
    if request.method == 'POST':
        form = CaseTypeForm(request.POST, instance=casetype)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = CaseTypeForm(instance=casetype)
    else:
        form = CaseTypeForm(instance=casetype)

    context = {
        'form': form,
        'sid': sid,
        'matters' : matters,
    }
    return render(request, 'reference_lookup/newCaseType.html', context)

def RemoveCaseType(request, pk):
    casetype = CaseType.objects.get(id=pk)
    casetype.delete()
    return redirect('reference-index')

def NewNature(request):
    if request.method == "POST":
        form = NatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-nature')
    else:
        form = NatureForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newNature.html', context)

def RemoveStageGroup(request, pk):
    stagegroup = ActivityGroup.objects.get(id=pk)
    stagegroup.delete()
    return redirect('reference-index')


def StageGroup(request):
    if request.method == 'POST':
        form = ActivityGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-activitygroup')
    else:
        form = ActivityGroupForm()
    
    context = {
        'form':form,
    }

    return render(request, 'reference_lookup/newActivityGroup.html', context)
        
def EditNature(request, pk):
    nature = NatureOfCase.objects.get(id=pk)
    matters = Matters.objects.filter(nature_id=pk).order_by('-modified_at')
    sid = pk
    if request.method == 'POST':
        form = NatureForm(request.POST, instance=nature)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = NatureForm(instance=nature)
    else:
        form = NatureForm(instance=nature)

    context = {
        'form': form,
        'sid': sid,
        'matters': matters,
    }
    return render(request, 'reference_lookup/newNature.html', context)

def EditStageGroup(request, pk):
    stage = ActivityGroup.objects.get(id=pk)
    if request.method == 'POST':
        form = ActivityGroupForm(request.POST, instance=stage)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = ActivityGroupForm(intance=stage)
    else:
        form = ActivityGroupForm(instance=stage)
    
    context = {
        'form' : form,
    }

    return render(request, 'reference_lookup/newActivityGroup.html', context)

def RemoveNature(request, pk):
    nature = NatureOfCase.objects.get(id=pk)
    nature.delete()
    return redirect('reference-index')

def NewAppearance(request):
    if request.method == "POST":
        form = AppearanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-taskcode')
    else:
        form = AppearanceForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newappearance.html', context)

def EditAppearance(request, pk):
    apperance = Appearance.objects.get(id=pk)
    matters = Matters.objects.filter(appearance_id=pk).order_by('-modified_at')
    sid = pk
    if request.method == 'POST':
        form = AppearanceForm(request.POST, instance=apperance)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = AppearanceForm(instance=apperance)
    else:
        form = AppearanceForm(instance=apperance)

    context = {
        'form': form,
        'sid': sid,
        'matters':matters,
    }
    return render(request, 'reference_lookup/newappearance.html', context)
def RemoveAppearance(request, pk):
    appearance = Appearance.objects.get(id=pk)
    appearance.delete()
    return redirect('reference-index')

def NewCourts(request):
    if request.method == "POST":
        form = CourtsCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-taskcode')
    else:
        form = CourtsCodeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newcourts.html', context)

def addfees(request):
    if request.method == 'POST':
        form = FilingFeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')

def EditCourts(request, pk):
    courts = Courts.objects.get(id=pk)
    matters = Matters.objects.filter(filed_at_id=pk).order_by('-modified_at')
    sid = pk
    if request.method == 'POST':
        form = CourtsCodeForm(request.POST, instance=courts)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            form = CourtsCodeForm(instance=courts)
    else:
        form = CourtsCodeForm(instance=courts)

    context = {
        'form': form,
        'sid': sid,
        'matters': matters,
    }
    return render(request, 'reference_lookup/newcourts.html', context)

def RemoveCourts(request, pk):
    courts = Courts.objects.get(id=pk)
    courts.delete()
    return redirect('reference-index')


def NewTaskCode(request):
    if request.method == "POST":
        form = ActivityCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-taskcode')
    else:
        form = ActivityCodeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newtaskcode.html', context)

def NewDueCode(request):
    if request.method == "POST":
        form = DueCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
        else:
            return redirect('new-taskcode')
    else:
        form = DueCodeForm()

    context = {
        'form': form,
    }

    return render(request, 'reference_lookup/newduecode.html', context)


def definefilingfees(request, pk):
    taskcode = ActivityCodes.objects.get(id=pk)
    print(taskcode)
    fees = FilingFeeCodes.objects.filter(ActivityCode_id = pk)
    form = FilingFeesForm()

    
    context = {
        'task' : taskcode,
        'fees' : fees,
        'form' : form,
    }
    return render(request, 'reference_lookup/definefees.html', context)

    

def EditTaskCode(request, pk):
    taskcode = ActivityCodes.objects.get(id=pk)
    fees = FilingFeeCodes.objects.filter(ActivityCode_id = pk)
    sid = pk
    if request.method == 'POST':
        form = ActivityCodeForm(request.POST, instance=taskcode)
        if form.is_valid():
            taskcode_rec = form.save(commit=False)
            taskcode_rec.save()
            code_id = taskcode_rec.id
            print(code_id)
            return redirect('define-fees', code_id)
        else:
            form = ActivityCodeForm(instance=taskcode)
    else:
        form = ActivityCodeForm(instance=taskcode)

    context = {
        'form': form,
        'sid': sid,
        'fees': fees,
    }
    return render(request, 'reference_lookup/newtaskcode.html', context)

def EditDueCode(request, pk):
    duecode = DueCode.objects.get(id=pk)
    sid = pk
    if request.method == 'POST':
        form = DueCodeForm(request.POST, instance=duecode)
        if form.is_valid():
            form.save()
            return redirect('reference-index')
            # taskcode_rec = form.save(commit=False)
            # taskcode_rec.save()
            # code_id = taskcode_rec.id
            # print(code_id)
            # return redirect('define-fees', code_id)
        else:
            form = DueCodeForm(instance=duecode)
    else:
        form = DueCodeForm(instance=duecode)

    context = {
        'form': form,
    }
    return render(request, 'reference_lookup/newduecode.html', context)

def RemoveTaskCode(request, pk):
    activity = ActivityCodes.objects.get(id=pk)
    activity.delete()
    return redirect('reference-index')

def RemoveDueCode(request, pk):
    duecode = DueCode.objects.get(id=pk)
    duecode.delete()
    return redirect('reference-index')
