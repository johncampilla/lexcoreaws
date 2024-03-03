from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from client.models import Client_Data
from matter.models import Matters, IP_Matter
from invoice.models import AccountsReceivable
from activity.forms import ActivityForm
from .models import *
from datetime import date, datetime, timedelta
from django.http import JsonResponse
from django.db.models import Q, Sum, Count
from django.contrib import messages
from django.views.generic import TemplateView

# more imports login/logout
# from django.contrib.auth import authenticate, login, logout #login/logout autentication
# from django.contrib.auth.decorators import login_required # Login Required
# from django.views.decorators.cache import cache_control #destroy the section after logout


# Create your views here.
today = date.today()
curr_month = today.month % 12
curr_year = today.year
prev_year  = today.year
prev_month = today.month -1
if prev_month == 0:
    prev_month = 12
    prev_year  = today.year -1 

# @login_required(login_url="/login/")
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    def apptypecount():
        apptype_count = Matters.objects.values('apptype__apptype').annotate(noofmatters = Count('apptype__apptype')) 
        NumberOfMattersByAppType.objects.all().delete()
        for data in apptype_count :
            applicationtype = data['apptype__apptype']
            count = data['noofmatters']
            apptypesummary = NumberOfMattersByAppType(applicationtype=applicationtype, count=count)
            apptypesummary.save()
    
    def lawyercount():
        lawyer_count = Matters.objects.values('handling_lawyer__access_code').annotate(noofmatters = Count('handling_lawyer__access_code')) 
        NumberOfMattersByLawyers.objects.all().delete()
        for data in lawyer_count :
            lawyers = data['handling_lawyer__access_code']
            count = data['noofmatters']
            apptypesummary = NumberOfMattersByLawyers(lawyer=lawyers, count=count)
            apptypesummary.save()
    
    def industrycount():
        industry_count = Client_Data.objects.values('industry__industry').annotate(noofmatters = Count('industry__industry'))
        NumberOfMattersByIndustry.objects.all().delete()
        for data in industry_count :
            industry = data['industry__industry']
            count = data['noofmatters']
            industrysummary = NumberOfMattersByIndustry(industry=industry, count=count)
            industrysummary.save()

    def foldercount():
        folder_count = Matters.objects.values('folder__folder_type__folder').annotate(noofmatters = Count('folder__folder_type__folder'))
        NumberOfMattersByFolder.objects.all().delete()
        for data in folder_count :
            folder = data['folder__folder_type__folder']
            count = data['noofmatters']
            foldersummary = NumberOfMattersByFolder(folder=folder, count=count)
            foldersummary.save()

    def casetypecount():
        casetype_count = Matters.objects.values('case_type__case_type').annotate(noofmatters = Count('case_type__case_type'))
        NumberOfMattersByCaseType.objects.all().delete()
        for data in casetype_count :
            casetype = data['case_type__case_type']
            count = data['noofmatters']
            casetypesummary = NumberOfMattersByCaseType(casetype=casetype, count=count)
            casetypesummary.save()
    
    def naturecount():
        nature_count = Matters.objects.values('nature__nature').annotate(noofmatters = Count('nature__nature'))
        NumberOfMattersByNature.objects.all().delete()
        for data in nature_count :
            nature = data['nature__nature']
            count = data['noofmatters']
            naturesummary = NumberOfMattersByNature(nature=nature, count=count)
            naturesummary.save()

    apptypecount()
    
    lawyercount()
    lawyerdata = NumberOfMattersByLawyers.objects.all().order_by('lawyer')
    industrycount()
    industrydata = NumberOfMattersByIndustry.objects.all().order_by('industry')
    foldercount()
    folderdata = NumberOfMattersByFolder.objects.all().order_by('folder')
    casetypecount()
    casetypedata = NumberOfMattersByCaseType.objects.all().order_by('casetype')
    naturecount()
    naturedata = NumberOfMattersByNature.objects.all().order_by('nature')

    if today.month == 1:
        prev_month = 12
        matters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = today.month)
        prevmatters = Matters.objects.filter(filing_date__year = today.year-1, filing_date__month = prev_month)
    else:        
        matters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = today.month)
        prevmatters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = today.month-1)
    
    if today.month == 1:
        prev_month = 12
        clients = Client_Data.objects.filter(date_acquired__year = today.year, date_acquired__month = today.month)
        prevclient = Client_Data.objects.filter(date_acquired__year = today.year-1, date_acquired__month = prev_month)
    else:
        clients = Client_Data.objects.filter(date_acquired__year = today.year, date_acquired__month = today.month)
        prevclient = Client_Data.objects.filter(date_acquired__year = today.year, date_acquired__month = today.month-1)

    if today.month == 1 : 
        prev_month = 12
        ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year, registration_date__month = today.month)
        prev_ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year-1, registration_date__month = prev_month)
    else:
        ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year, registration_date__month = today.month)
        prev_ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year, registration_date__month = today.month-1)
    

# Accounts Receivables

    bill_amount = AccountsReceivable.objects.filter(bill_date__year = today.year, bill_date__month = today.month).exclude(payment_tag="CN").aggregate(Sum('total_USDamount'))
    bill_amt = bill_amount["total_USDamount__sum"]

    prev_bill_amount = AccountsReceivable.objects.filter(bill_date__year = prev_year, bill_date__month = today.month-1).exclude(payment_tag="CN").aggregate(Sum('total_USDamount'))
    prev_bill_amt = prev_bill_amount["total_USDamount__sum"]

    peso_amount = AccountsReceivable.objects.filter(bill_date__year = today.year, bill_date__month = today.month).exclude(payment_tag="CN").aggregate(Sum('total_PhPamount'))
    peso_amt = peso_amount["total_PhPamount__sum"]

    prev_peso_amount = AccountsReceivable.objects.filter(bill_date__year =prev_year, bill_date__month = today.month-1).exclude(payment_tag="CN").aggregate(Sum('total_PhPamount'))
    prev_peso_amt = prev_peso_amount["total_PhPamount__sum"]

    Unbill_amount = AccountsReceivable.objects.filter(payment_tag = 'UN').aggregate(Sum('total_USDamount'))
    unbill_amt = Unbill_amount["total_USDamount__sum"]



    clientcount = clients.count()
    matterscount = matters.count()

    prevmonthmatters = prevmatters.count()
    prevclientcount = prevclient.count()

    ip_issuacecount = ip_issuance_cert.count()
    prev_ip_issuance_cert = prev_ip_issuance_cert.count()

    
    form = ActivityForm()

    context = {
        'lawyerdata'  : lawyerdata,
        'industrydata': industrydata,
        'folderdata': folderdata,
        'casetypedate': casetypedata,

        'clientcount' : clientcount,
        'prevclientcount' : prevclientcount,

        'matterscount' : matterscount,
        'prevmonthmatters' : prevmonthmatters,

        'issuancecount': ip_issuacecount,
        'previssuancecount' : prev_ip_issuance_cert,

        'bill_amt' : bill_amt,
        'prev_bill_amt' : prev_bill_amt,
        'peso_amt' : peso_amt,
        'prev_peso_amt' : prev_peso_amt,
        'unbill_amt': unbill_amt,
        'form' : form,
        'rundate':today,
    }
                                                                    
#    return render(request, 'dashboard/index-chart.html', context)
    return render(request, 'dashboard/dashboard.html', context)

def details_ip_issuance(request):
    if today.month == 1 : 
        prev_month = 12
        ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year, registration_date__month = today.month)
        prev_ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year -1, registration_date__month = prev_month)
    else:
        ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year, registration_date__month = today.month)
        prev_ip_issuance_cert = IP_Matter.objects.filter(registration_date__year = today.year, registration_date__month = today.month-1)


    context = {
        'issuance_cert' : ip_issuance_cert,
        'prev_issuance_cert' :prev_ip_issuance_cert
    }
    return render(request, 'dashboard/viewnewcertifcates.html', context)

def details_newbills(request):
    invoices = AccountsReceivable.objects.filter(bill_date__year = today.year, bill_date__month = today.month)
    previnvoices = AccountsReceivable.objects.filter(bill_date__year = today.year, bill_date__month = prev_month)

    context = {
        'invoices' : invoices,
        'previnvoices' : previnvoices,
    }

    return render(request, 'dashboard/viewnewbills.html', context)

def details_new_clients(request):

    if today.month == 1:
        prev_month = 12
        clients = Client_Data.objects.filter(date_acquired__year = today.year, date_acquired__month = today.month)
        prevclient = Client_Data.objects.filter(date_acquired__year = today.year-1, date_acquired__month = prev_month)
    else:
        clients = Client_Data.objects.filter(date_acquired__year = today.year, date_acquired__month = today.month)
        prevclient = Client_Data.objects.filter(date_acquired__year = today.year, date_acquired__month = today.month-1)

    
    context = {
        'clients': clients,
        'prevclients':prevclient,
    }
    return render(request, 'dashboard/viewnewclients.html', context)

def details_new_matters(request):
    if today.month == 1:
        prev_month = 12
        matters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = today.month)
        prevmatters = Matters.objects.filter(filing_date__year = today.year-1, filing_date__month = prev_month)
    else:        
        matters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = today.month)
        prevmatters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = today.month-1)

    # matters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = today.month)
    # prevmatters = Matters.objects.filter(filing_date__year = today.year, filing_date__month = prev_month)

    context = {
        'matters':matters,
        'prevmatters':prevmatters,
    }
    return render(request, 'dashboard/viewnewmatters.html', context)

def searchlist(request):
    #username = request.user.username
    #lawyers = request.user.user_profile.supporto
    #listoflawyers = lawyers.split(',')
    # code1 = ""
    # code2 = ""
    # code3 = ""
    # code4 = ""
    # code5 = ""
    # code6 = ""
    # code7 = ""

    # for i in range(0, len(listoflawyers)):
    #     if i == 0:
    #         code1 = listoflawyers[i]
    #     elif i == 1:
    #         code2 = listoflawyers[i]
    #     elif i == 2:
    #         code3 = listoflawyers[i]
    #     elif i == 3:
    #         code4 = listoflawyers[i]
    #     elif i == 4:
    #         code5 = listoflawyers[i]
    #     elif i == 5:
    #         code6 = listoflawyers[i]
    #     elif i == 6:
    #         code7 = listoflawyers[i]

    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(matter_title__icontains=q) | Q(folder__client__client_name__icontains=q) | 
                     Q(handling_lawyer__access_code=q) | Q(folder__folder_description__icontains=q) | Q(referenceno__icontains=q))
        

        matters = Matters.objects.filter(
            multiple_q).order_by("folder__client__client_name")
        
    else:
        
        matters = Matters.objects.all().order_by("folder__client__client_name")


    context = {
        'matters': matters,
    }
    return render(request, 'dashboard/searchlist.html', context)

def reports(request):
    return render(request, 'dashboard/reports.html')

def totalcountindustry(request):
   queryset = NumberOfMattersByIndustry.objects.all()
   dct = {
       "labels": [],
       "data": []
   }
   for item in queryset:
       dct["labels"].append(item.industry)
       dct["data"].append(item.count)

   return JsonResponse(dct)

def printindustrycount(request):
    queryset = NumberOfMattersByIndustry.objects.all().order_by('-count')

    context = {
        'queryset' :queryset,
    }
    return render(request, 'dashboard/industrycount.html', context)


def totalcountapptype(request):
   queryset = NumberOfMattersByAppType.objects.all()
   dct = {
       "labels": [],
       "data": []
   }
   for item in queryset:
       dct["labels"].append(item.applicationtype)
       dct["data"].append(item.count)

   return JsonResponse(dct)

def printapptypecount(request):
    queryset = NumberOfMattersByAppType.objects.all().order_by('-count')

    context = {
        'queryset' :queryset,
    }
    return render(request, 'dashboard/apptypecount.html', context)

def totalcountlawyers(request):
   queryset =  NumberOfMattersByLawyers.objects.all()
   dct = {
       "labels": [],
       "data": []
   }
   for item in queryset:
       dct["labels"].append(item.lawyer)
       dct["data"].append(item.count)

   return JsonResponse(dct)

def printlawyercount(request):
    queryset = NumberOfMattersByLawyers.objects.all().order_by('-count')

    context = {
        'queryset' :queryset,
    }
    return render(request, 'dashboard/lawyercount.html', context)

def totalcasefolders(request):
   queryset =  NumberOfMattersByFolder.objects.all()
   dct = {
       "labels": [],
       "data": []
   }
   for item in queryset:
       dct["labels"].append(item.folder)
       dct["data"].append(item.count)

   return JsonResponse(dct)

def printfoldercount(request):
    queryset = NumberOfMattersByFolder.objects.all().order_by('-count')

    context = {
        'queryset' :queryset,
    }
    return render(request, 'dashboard/foldercount.html', context)

def totalcasetype(request):
   queryset =  NumberOfMattersByCaseType.objects.all()
   dct = {
       "labels": [],
       "data": []
   }
   for item in queryset:
       dct["labels"].append(item.casetype)
       dct["data"].append(item.count)

   return JsonResponse(dct)

def printcasetypecount(request):
    queryset = NumberOfMattersByCaseType.objects.all().order_by('-count')

    context = {
        'queryset' :queryset,
    }
    return render(request, 'dashboard/casetypecount.html', context)

def totalnature(request):
   queryset =  NumberOfMattersByNature.objects.all()
   dct = {
       "labels": [],
       "data": []
   }
   for item in queryset:
       dct["labels"].append(item.nature)
       dct["data"].append(item.count)

   return JsonResponse(dct)

def printnaturecount(request):
    queryset = NumberOfMattersByNature.objects.all().order_by('-count')

    context = {
        'queryset' :queryset,
    }
    return render(request, 'dashboard/naturecount.html', context)

# details of summary

def detailapplicationtype(request, selected):
    queryset = Matters.objects.filter(apptype__apptype = selected)
    context = {
        'queryset' : queryset,
    }
    return render(request, 'dashboard/apptypelist.html', context)

def detailindustry(request, selected):
    queryset = Client_Data.objects.filter(industry__industry = selected)
    context = {
        'queryset' : queryset,
    }
    return render(request, 'dashboard/industrylist.html', context)

def detaillawyers(request, selected):
    queryset = Matters.objects.filter(handling_lawyer__access_code = selected)
    context = {
        'queryset' : queryset,
    }
    return render(request, 'dashboard/lawyerslist.html', context)

def detailfolders(request, selected):
    queryset = Matters.objects.filter(folder__folder_type__folder = selected)
    context = {
        'queryset' : queryset,
    }
    return render(request, 'dashboard/folderlist.html', context)

def detailcasetype(request, selected):
    queryset = Matters.objects.filter(case_type__case_type = selected)
    context = {
        'queryset' : queryset,
    }
    return render(request, 'dashboard/casetypelist.html', context)

def newactivity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 



# login function

# def Login(request):
#     if request.user == None or request.user == "" or request.user.username=="":
#         return render(request, 'dashboard/login.html')
#     else:
#         return HttpResponseRedirect('/')
    

# # login user

# def LoginUser(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username = username, password=password)
#         print(user)
#         if user != None:
#             print("pasok password")
#             login(request, user)
#             return HttpResponseRedirect('/')
#         else:
#             print("d2 ka kasi pumasok")
#             messages.error(request, "Enter your data correctly.")
#             return HttpResponseRedirect('/')

# # logout function

# def LogoutUser(request):
#     logout(request)
#     request.user = None
#     return HttpResponseRedirect('/')