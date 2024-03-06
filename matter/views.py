from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from matter.models import CaseHistory
from activity.models import task_detail, FilingDocs
from invoice.models import AccountsReceivable
from emailportal.models import Emails, EmailAttachments
from emailportal.forms import NewEmailForm, EmailAttachForm
from chatter.models import inboxmessage
from .forms import *
from casefolder.forms import *
from activity.forms import filingdocforms, DocumentEditForm
from reference_lookup.forms import ClGoodsProfileForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import string
from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required
def MatterList(request):
    matters = Matters.objects.all().order_by("-created_at")
    form = EditMatterForm()

    context = {
        'matters' : matters, 
        'form' : form,
    }
    return render(request, 'matter/index.html', context)

@login_required
def SelectMatter(request, pk):
    matter = Matters.objects.get(id=pk)
    duedates = AppDueDate.objects.filter(matter_id = pk)
    sid = matter.case_type.id
    stype = CaseType.objects.get(id=sid)
    apptype_id = matter.apptype.id
    sapptype = AppType.objects.get(id=apptype_id)
    documents = FilingDocs.objects.filter(task_detail__matter_id = pk)
    emails = Emails.objects.filter(matter_id = pk).order_by('-created_at')
    chat = inboxmessage.objects.filter(see_matter_id = pk).order_by('-created_at')
    
    
    try:
        ip_matter = IP_Matter.objects.get(matter_id = pk)
    except IP_Matter.DoesNotExist:
        ip_matter = None

    activities = task_detail.objects.filter(matter_id = pk)
    casetheory = CaseDescription.objects.filter(matter_id = pk)
    caseevidence = CaseEvidence.objects.filter(matter_id = pk)
    casehistory = CaseHistory.objects.filter(matter_id = pk)
    priorityclaims = ConventionPriority.objects.filter(matter_id = pk)
    applicants = Matter_Applicant.objects.filter(matter_id = pk)
    inventors = Matter_Inventor.objects.filter(matter_id = pk)
    services = Matter_ClassOfGoods.objects.filter(matter_id = pk)
    invoices = AccountsReceivable.objects.filter(matter_id = pk).order_by('-bill_date')
    image = IP_MatterImage.objects.filter(matter_id = pk)

    form = MatterForm()
    forminfo = IP_MatterForm()
    formpriority = PriorityForm()
    formapplicant = ApplicantForm()
    formClGoods = ClGoodsForm()
    formDueDate = NewDueDateForm()
    forminventor = MatterInventorForm()

    context = {
        'matter' : matter,
        'duedates' : duedates,
        'ip_matter' : ip_matter, 
        'activities' : activities,
        'casetheory' : casetheory,
        'caseevidence'  : caseevidence,
        'priorityclaims' : priorityclaims,
        'applicants' : applicants,
        'inventors' : inventors,
        'services': services,
        'form'  : form,
        'forminfo': forminfo,
        'formpriority':formpriority,
        'formapplicant':formapplicant,
        'formClGoods': formClGoods,
        'formDueDate': formDueDate,
        'invoices' : invoices,
        'image'    : image,
        'casehistory': casehistory,
        'documents': documents,
        'forminventor' : forminventor,
        'emails' : emails,
        'msginbox' : chat,
    }
    if stype.case_type.upper() == 'IP FILINGS':
        if  sapptype.apptype.upper() == "TRADEMARK" : 
            return render(request, 'matter/matter_detail_ip_TM.html', context)
        elif sapptype.apptype.upper() == "INVENTION" :
            return render(request, 'matter/matter_detail_ip_INV.html', context)
        elif sapptype.apptype.upper() == "PCT" :
            return render(request, 'matter/matter_detail_ip_INV.html', context)
        elif sapptype.apptype.upper() == "DESIGN" :
            return render(request, 'matter/matter_detail_ip_DESIGN.html', context)
        elif sapptype.apptype.upper() == "UTILITY MODEL" :
            return render(request, 'matter/matter_detail_ip_INV.html', context)
        else :
            print("d2 pumasok")
            return render(request, 'matter/matter_detail_nonip.html', context)

    else:
        return render(request, 'matter/matter_detail_nonip.html', context)
    
@login_required        
def newfolder(request):
    if request.method == 'POST':
        form = CaseFolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new-matter')
        else:
            form = CaseFolderForm()
    else:
        form = CaseFolderForm()
    
    context = {
        'form':form,
    }
    return render(request, 'matter/newfolder.html', context)

@login_required
def NewDueDateModal(request):
    if request.method == 'POST':
        form = NewDueDateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
@login_required
def NewClassOfGoods(request):
    if request.method == 'POST':
        form = ClGoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('select-matter', request.POST['matter'])

@login_required
def NewMatterApplicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant_rec = form.save(commit=False)
            applicant_rec.matter_id = request.POST['matter']
            applicant_rec.save()            
            return redirect('select-matter', request.POST['matter'])

@login_required        
def NewMatterInventor(request):
    if request.method == 'POST':
        form = MatterInventorForm(request.POST)
        if form.is_valid():
            applicant_rec = form.save(commit=False)
            applicant_rec.matter_id = request.POST['matter']
            applicant_rec.save()            
            return redirect('select-matter', request.POST['matter'])

@login_required
def NewApplicantModal(request):
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-applicants')

@login_required
def NewInventorModal(request):
    if request.method == 'POST':
        form = InventorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matter-list')
#            return HttpResponseRedirect('/')

@login_required
def viewapplicants(request):
    applicants = Applicant.objects.all().order_by('applicant')
    form = ApplicantProfileForm()
    context = {
        'applicants': applicants,
        'form': form,
    }
    return render(request, 'matter/listofapplicants.html', context)

@login_required
def viewinventors(request, mid):
    inventors = Inventor.objects.all().order_by('last_name')
    matter = Matters.objects.get(id=mid)
    form = InventorForm()
    context = {
        'inventors': inventors,
        'form': form,
        'mid':mid,
        'matter' : matter,
    }
    return render(request, 'matter/listofinventors.html', context)

@login_required
def viewclassofgoods(request, pk):
    matter = Matters.objects.get(id=pk)
    classofgoods = ClassOFGoods.objects.all().order_by('nice_class')
    form = ClGoodsProfileForm()
    context = {
        'form': form,
        'matter': matter,
        'classofgoods' : classofgoods,
        'pk':pk
    }
    return render(request, 'matter/listofgoods.html', context)

@login_required
def newclgoodsprofile(request):
    if request.method == 'POST':
        form = ClGoodsProfileForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('select-matter', request.POST['matter'])    
@login_required
def NewPriority_modal(request):
    if request.method == 'POST':
        form = PriorityForm(request.POST)
        if form.is_valid():
            priority_rec = form.save(commit=False)
            priority_rec.matter_id = request.POST['matter']
            priority_rec.save()            
#            form.save()
            # return HttpResponseRedirect('/')
            return redirect('select-matter', request.POST['matter'])

@login_required
def NewMatter(request):
    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            matter_rec = form.save(commit=False)
            matter_rec.folder_id = request.POST['folder']
            matter_rec.save()            
            return redirect('matter-list')
        
@login_required
def NewMatterInfo(request):
    if request.method == 'POST':
        form = IP_MatterForm(request.POST)
        if form.is_valid():
            IPMatter_rec = form.save(commit=False)
            IPMatter_rec.matter_id = request.POST['matter']
            IPMatter_rec.save()            
            # return redirect('select-matter', request.POST['matter'])
            return HttpResponseRedirect('/')

@login_required
def NewDueDate(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = DueDateForm(request.POST)
        if form.is_valid():
            duedate_rec = form.save(commit=False)
            duedate_rec.matter_id = matter.id
            duedate_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            form = DueDateForm()
    else:
        form = DueDateForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newduedate.html', context)   
@login_required
def EditMatter(request, pk):
    matter = Matters.objects.get(id=pk)
    activities = task_detail.objects.filter(matter_id = pk)
    sid = matter.case_type.id
    stype = CaseType.objects.get(id=sid)
    apptype_id = matter.apptype.id
    sapptype = AppType.objects.get(id=apptype_id)
    image = IP_MatterImage.objects.filter(matter_id = pk)

    if request.method == 'POST':
        form = EditMatterForm(request.POST, instance=matter)
        if form.is_valid():
            form.save()
            if sapptype.apptype == "NON-IP":
                print('NONIP')
                return redirect('edit-matter', matter.id)
            else :
                print('IP')
                return redirect('edit-ipmatter', matter.id)
            
        else:
            form = EditMatterForm(instance=matter)
    else:
        form = EditMatterForm(instance=matter)
    
    context = {
        'form' : form,
        'matter' : matter,
        'sapptype' : sapptype, 
        'activities' : activities,  
        'image': image,    
    }    

    return render(request, 'matter/edit_matter.html', context)   

@login_required
def Edit_IPMatter(request, pk):
    def computeduedate():
        for duecode in duecodes:
            sdate = None
            if duecode.fieldbsis == 'Application Date':
                sdate = ip_matter.application_date
            if duecode.fieldbsis == 'Publication Date':
                sdate = ip_matter.publication_date
            if duecode.fieldbsis == 'Registration Date':
                sdate = ip_matter.registration_date
            if duecode.fieldbsis == 'Priority Date':
                sdate = ip_matter.priority_date
            if duecode.fieldbsis == 'PCT Filing Date':
                sdate = ip_matter.pct_appdate
            if duecode.fieldbsis == 'PCT Publication Date':
                sdate = ip_matter.pct_pubdate
            if duecode.fieldbsis == 'Renewal Date':
                sdate = ip_matter.renewal_date
            if duecode.fieldbsis == 'IR Date':
                sdate = ip_matter.IR_date
            if duecode.fieldbsis == 'IR Renewal Date':
                sdate = ip_matter.IR_renewalDate
            if sdate:
                if duecode.basisofcompute == 'In Years':
                    nyears = int(duecode.terms)
                    svalue = ("+"+str(nyears))
                    duedate = sdate + relativedelta(years=int(svalue))

                if duecode.basisofcompute == 'In Months':
                    nmonth = int(duecode.terms)
                    svalue = ("+"+str(nmonth))
                    duedate = sdate + relativedelta(months=int(svalue))

                if duecode.basisofcompute == 'In Days':
                    ndays = int(duecode.terms)
                    svalue = ("+"+str(ndays))
                    duedate = sdate + relativedelta(days=int(svalue))
                    
                dues = AppDueDate.objects.filter(matter_id=ipmatter_rec.matter_id, duedate=duedate)
                if dues.exists():
                    pass
                else:
                    duedates = AppDueDate(matter_id=ipmatter_rec.matter_id, duedate=duedate, duecode_id = duecode.id, particulars=duecode.Description)
                    duedates.save()

    matter = Matters.objects.get(id=pk)
    apptype_id = matter.apptype.id
    sapptype = AppType.objects.get(id=apptype_id)
    duecodes = DueCode.objects.filter(apptype = sapptype)
    try:
        ip_matter = IP_Matter.objects.get(matter_id = pk)
        sappdate = ip_matter.application_date
    except IP_Matter.DoesNotExist:
        ip_matter = None

    apptype_id = matter.apptype.id
    sapptype = AppType.objects.get(id=apptype_id)
    if request.method == 'POST':
        form = Edit_IPTMMatterForm(request.POST, instance = ip_matter)
        if form.is_valid():
            ipmatter_rec = form.save(commit=False)
            ipmatter_rec.matter_id = request.POST['matter']
            ipmatter_rec.save() 
            computeduedate()
            return redirect('select-matter', matter.id)
        else:
            form = Edit_IPTMMatterForm(instance=ip_matter)
    else:
        form = Edit_IPTMMatterForm(instance=ip_matter)
    
    context = {
        'form' : form,
        'matter' : matter,
        'sapptype' : sapptype, 
        'ip_matter' : ip_matter,      
    }    

    return render(request, 'matter/edit_ipmatter.html', context)   

@login_required
def EditDueDate(request, pk, mid):
    duedate = AppDueDate.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = DueDateForm(request.POST, instance=duedate)
        if form.is_valid():
            form.save()
            return redirect('select-matter', mid)
        else:
            form = DueDateForm(instance=duedate)
    else:
        form = DueDateForm(instance=duedate)

    context = {
        'form': form,
        'sid': sid,
        'matter':matter,
    }
    return render(request, 'matter/editduedate.html', context)

@login_required
def EditClassOfGoods(request, pk, mid):
    clgoods = Matter_ClassOfGoods.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = EditClGoodsForm(request.POST, instance=clgoods)
        if form.is_valid():
            form.save()
            return redirect('select-matter', mid)
        else:
            form = EditClGoodsForm(instance=clgoods)
    else:
        form = EditClGoodsForm(instance=clgoods)

    context = {
        'form': form,
        'sid': sid,
        'matter':matter,
    }
    return render(request, 'matter/editclgoods.html', context)

@login_required
def RemoveClassGoods(request, pk, mid):
    classofgoods = Matter_ClassOfGoods.objects.get(id=pk)
    classofgoods.delete()
    return redirect('select-matter', mid)

@login_required
def RemoveDueDate(request, pk, mid):
    duedate = AppDueDate.objects.get(id=pk)
    duedate.delete()
    return redirect('select-matter', mid)

@login_required
def NewApplicant(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            duedate_rec = form.save(commit=False)
            duedate_rec.matter_id = matter.id
            duedate_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            form = ApplicantForm()
    else:
        form = ApplicantForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newapplicant.html', context)   

@login_required
def EditMatterApplicant(request, pk, mid):
    applicant = Matter_Applicant.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = EditApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            applicant_rec = form.save(commit=False)
            applicant_rec.matter_id = matter.id
            applicant_rec.save()            
            return redirect('select-matter', mid)
        else:
            form = ApplicantForm(instance=applicant)
    else:
        form = ApplicantForm(instance=applicant)

    context = {
        'form': form,
        'sid': sid,
        'matter':matter,
        'applicant': applicant
    }
    return render(request, 'matter/editmatterapplicant.html', context)   

@login_required
def NewApplicantProfile(request, mid):
    applicantlist = Applicant.objects.all().order_by('applicant')
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new-applicantprofile', mid)
        else:
            form = ApplicantProfileForm()
    else:
        form = ApplicantProfileForm()

    context = {
        'form': form,
        'applicantlist':applicantlist,
        'mid':mid,
    }
    return render(request, 'matter/newapplicantprofile.html', context)   

@login_required
def EditApplicant(request, pk):
    applicant = Applicant.objects.get(id=pk)
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('view-applicants')
        else:
            form = ApplicantProfileForm(instance=applicant)
    else:
        form = ApplicantProfileForm(instance=applicant)

    context = {
        'form': form,
        'applicant': applicant,

    }
    return render(request, 'matter/editapplicant.html', context)

@login_required
def Delete_Applicant(request, pk, mid):
    applicant = Applicant.objects.get(id=pk)
    applicant.delete()
    return redirect('select-matter', mid)

@login_required
def Delete_MatterApplicant(request, pk, mid):
    applicant = Matter_Applicant.objects.get(id=pk)
    applicant.delete()
    return redirect('select-matter', mid)

@login_required
def NewCaseDescription(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = NewCaseDescriptionForm(request.POST)
        if form.is_valid():
            casedescription_rec = form.save(commit=False)
            casedescription_rec.matter_id = matter.id
            casedescription_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            form = NewCaseDescriptionForm()
    else:
        form = NewCaseDescriptionForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newcasedescription.html', context)   

# def NewCaseHistory(request, mid):
#     matter = Matters.objects.get(id=mid)
#     if request.method == 'POST':
#         form = NewProceduralHistoryForm(request.POST)
#         if form.is_valid():
#             casehistory_rec = form.save(commit=False)
#             casehistory_rec.matter_id = matter.id
#             casehistory_rec.save()
#             return redirect('select-matter', mid)
#         else:
#             form = NewProceduralHistoryForm()
#     else:
#         form = NewProceduralHistoryForm()
    
#     context = {
#         'form' : form,
#         'matter': matter,
#     }
#     return render(request, 'matter/newcasehistory.html', context)   

@login_required
def NewCaseEvidence(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = NewCaseEvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            caseeveidence_rec = form.save(commit=False)
            caseeveidence_rec.matter_id = matter.id
            caseeveidence_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            form = NewCaseEvidenceForm()
    else:
        form = NewCaseEvidenceForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newcaseEvidence.html', context)   

@login_required
def ViewEvidence(request, pk, mid):
    evidence = CaseEvidence.objects.get(id=pk)
    matter = Matters.objects.get(id=mid)
    form = NewCaseEvidenceForm(instance=evidence)
    if request.method == "POST":
        form = NewCaseEvidenceForm(request.POST, request.FILES, instance=evidence)
        if form.is_valid():
            form.save()
            return redirect('select-matter', mid)
        else:
            form = NewCaseEvidenceForm(instance=evidence)
    else:
        form = NewCaseEvidenceForm(instance=evidence)

    context = {
        'evidence':evidence,
        'matter':matter,
        'form' : form,
    }
    return render(request, 'matter/viewevidence.html', context)

@login_required
def NewPriority(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = NewPriorityForm(request.POST)
        if form.is_valid():
            priority_rec = form.save(commit=False)
            priority_rec.matter_id = matter.id
            priority_rec.save()            
            return redirect('select-matter', mid)
        else:
            form = NewPriorityForm()
    else:
        form = NewPriorityForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/new_priority.html', context)

@login_required
def NewActivity(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity_rec = form.save(commit=False)
            activity_rec.matter_id = matter.id
            activity_rec.save()            
            return redirect('select-matter', mid)
        else:
            form = ActivityForm()
    else:
        form = ActivityForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newactivity.html', context)   

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
    return render(request, 'matter/view_activity.html', context)

@login_required
def AttachDocument(request, pk):
    task = task_detail.objects.get(id=pk)
    matter = Matters.objects.get(id = task.matter_id)
    user_name = request.user.username

    if request.method == 'POST':
        form = filingdocforms(request.POST, request.FILES)
        if form.is_valid():
            document_rec = form.save(commit=False)
            document_rec.task_detail_id = task.id
            document_rec.createdby = user_name
            document_rec.save()            
            return redirect('select-matter', task.matter_id)
        else:
            form = filingdocforms()
    else:
        form = filingdocforms()

    context = {
        'form': form,
        'matter':matter,
        'task' : task,
    }
    return render(request, 'matter/newactivitydocs.html', context) 

@login_required
def deleteimage(request, pk):
    matterimage = IP_MatterImage.objects.get(id=pk)
    if matterimage : 
        mid = matterimage.matter_id
        matterimage.delete()
        return redirect('edit-matter', mid)

@login_required   
def addimage(request, pk):
    matter = Matters.objects.get(id=pk)
    if request.method == 'POST':
        form = IPImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_rec = form.save(commit=False)
            image_rec.matter_id = request.POST['matter']
            image_rec.save()            
            return redirect('edit-matter', matter.id)
        else:
            form = IPImageForm()
    else:
        form = IPImageForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'matter/newIPImageDocs.html', context)   

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
            return redirect('select-matter', matter.id)
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
    return render(request, 'matter/newactivitydocs.html', context)   
@login_required
def editimage(request, pk):
    matterimage = IP_MatterImage.objects.get(id=pk) 
    matter = Matters.objects.get(id = matterimage.matter_id) 

    form = IPImageForm(instance=matterimage)
    if request.method == "POST":
        form = IPImageForm(request.POST, request.FILES, instance=matterimage)
        if form.is_valid():
            form.save()            
            return redirect('edit-matter', matter.id)
        else:
            form = IPImageForm(instance=matterimage)
    else:
        form = IPImageForm(instance=matterimage)

    context = {
        'matter':matter,
        'form' : form,
        'matterimage' : matterimage,
    }
    return render(request, 'matter/editmatterimage.html', context)   

@login_required
def EditActivity(request, pk, mid):
    activity = task_detail.objects.get(id=pk)
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('select-matter', matter.id)
        else:
            form = ActivityForm(instance=activity)
    else:
        form = ActivityForm(instance=activity)
    context = {
        'form' : form,
        'matter' : matter,
        'activity' : activity,
    }
    return render(request, 'matter/editactivity.html', context)

@login_required
def EditPriority(request, pk, mid):
    priority = ConventionPriority.objects.get(id=pk)
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = EditPriorityForm(request.POST, instance=priority)
        if form.is_valid():
            priority_rec = form.save(commit=False)
            priority_rec.matter_id = matter.id
            priority_rec.save()            
            return redirect('select-matter', mid)
        else:
            form = EditPriorityForm(instance=priority)
    else:
        form = EditPriorityForm(instance=priority)

    context = {
        'form': form,
        'priority': priority,
        'matter' : matter,
    }
    return render(request, 'matter/editmatterpriority.html', context)

@login_required
def RemoveMatterPriority(request, pk, mid):
    priority = ConventionPriority.objects.get(id=pk)
    priority.delete()
    return redirect('select-matter', mid)

@login_required
def view_email(request, pk):
    form = NewEmailForm()
    email = Emails.objects.get(id = pk)
    matter = Matters.objects.get(id = email.matter_id)
    emailattachments = EmailAttachments.objects.filter(email_id = pk)
    print(emailattachments)

    context = {
        'email': email,
        'emailattachments' : emailattachments,
        'matter': matter,
    }

    return render(request, 'matter/selectedemail.html', context)

@login_required
def viewattachemail(request, pk):

    emaildoc = EmailAttachments.objects.get(id = pk)
    form = EmailAttachForm(instance=emaildoc)

    context = {
        'form' : form,
        'emaildoc' : emaildoc,
    }

    return render(request, 'matter/viewattachemail.html', context)




