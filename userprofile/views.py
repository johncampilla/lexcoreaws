from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, UserForm, userloginform, OTPForm, LawyerDataForm, EditUserProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import User_Profile
from matter.models import Matters, AppDueDate
from casefolder.models import Lawyer_Data
from activity.models import task_detail
from django.contrib import messages
from .utils import send_otp
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


import pyotp

# Create your views here.
@login_required
def index(request):
    return render(request, 'user/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {
        'form' : form
    }
    return render(request, 'user/register.html', context)

@login_required
def mylogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard-index')
    context = {
        'form' : form,
    }

    return render(request, 'user/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def userlist(request):
    #users_lawyers = User_Profile.objects.all()
    users_lawyers = User_Profile.objects.filter(rank='ASSOCIATES') | User_Profile.objects.filter(rank='MANAGING PARTNER') | User_Profile.objects.filter(rank='PARTNER')

    users_nonlawyers = User_Profile.objects.filter(rank='MIS STAFF') | User_Profile.objects.filter(rank='SYSTEM ADMIN') | User_Profile.objects.filter(rank='SECRETARY')

    form = UserForm()
    context = {
        'users' : users_lawyers,
        'non_lawyers' : users_nonlawyers,
        'form' : form,
    }
    return render(request, 'user/userlist.html', context)

@login_required
def newuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-user')

@login_required            
def lawyerinfo(request, pk):
    try:
        lawyer = Lawyer_Data.objects.get(lawyerID_id = pk)
    except Lawyer_Data.DoesNotExist:
        lawyer = None
    
    if lawyer:
        if request.method == 'POST':
            form = LawyerDataForm(request.POST, instance=lawyer)
            if form.is_valid():
                form.save()
                return redirect('define-userinfo', pk)
            else:
                form = LawyerDataForm(instance=lawyer)
        else:
            form = LawyerDataForm(instance=lawyer)

        context = {

            'form': form,
            'lawyer':lawyer,
        }

    else:
        if request.method == 'POST':
            form = LawyerDataForm(request.POST)
            if form.is_valid():
                lawyer_rec = form.save(commit=False)
                lawyer_rec.lawyerID_id = pk 
                lawyer_rec.save()
                return redirect('define-userinfo', pk)
            else:
                form = LawyerDataForm()
        else:
            form = LawyerDataForm()

        context = {

            'form': form,
            'lawyer':lawyer,
        }

    return render(request, 'user/editlawyer.html', context)

def edituser(request, pk):
    userprofile = User_Profile.objects.get(id = pk)
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
           form.save() 
           return redirect('define-userinfo', pk)
        else:
            form = EditUserProfileForm(instance=userprofile)
    else:
        form = EditUserProfileForm(instance=userprofile)
    
    context = {
        'form':form,
        'userprofile':userprofile,
    }

    return render(request, 'user/edituserprofile.html', context)

def addlawyer(request, pk):
    try:
        lawyerprofile = Lawyer_Data.objects.get(lawyerID_id = pk)
    except Lawyer_Data.DoesNotExist: 
        lawyerprofile = None  

    if not lawyerprofile:
        if request.method == 'POST':
            form = LawyerDataForm(request.POST)
            if form.is_valid():
                lawyer_rec = form.save(commit=False)
                lawyer_rec.lawyerID_id = pk
                lawyer_rec.save() 
                return redirect('define-userinfo', pk)
            else:
                form = LawyerDataForm()
        else:
            form = LawyerDataForm()
        
        context = {
            'form' : form,
            'lawyerprofile': lawyerprofile,
        }
        return render(request, 'user/newlawyer.html', context)
    else:
        return redirect('define-userinfo', pk)

def editlawyer(request, pk):
    try:
        lawyerprofile = Lawyer_Data.objects.get(lawyerID_id = pk)
    except Lawyer_Data.DoesNotExist: 
        lawyerprofile = None  

    if lawyerprofile:
        if request.method == 'POST':
            form = LawyerDataForm(request.POST, instance=lawyerprofile)
            if form.is_valid():
                form.save() 
                return redirect('define-userinfo', pk)
            else:
                form = LawyerDataForm(instance=lawyerprofile)
        else:
            form = LawyerDataForm(instance=lawyerprofile)
        
        context = {
            'form':form,
        }
    else:
        if request.method == 'POST':
            form = LawyerDataForm(request.POST)
            if form.is_valid():
                lawyerdata_rec = form.save(commit=False)
                lawyerdata_rec.lawyerID_id = pk
                lawyerdata_rec.save() 
                return redirect('define-userinfo', pk)
            else:
                form = LawyerDataForm()
        else:
            form = LawyerDataForm()
        
        context = {
            'form':form,
        }


    return render(request, 'user/editlawyer.html', context)




@login_required
def removeuser(request, pk):
    user = User_Profile.objects.get(id = pk)
    user.delete()
    return redirect('list-user')


def userinfo(request, pk):
    user = User_Profile.objects.get(id = pk)

    try:
        lawyer = Lawyer_Data.objects.get(lawyerID_id = pk)
        matters = Matters.objects.filter(handling_lawyer_id = lawyer.id)
        tasks = task_detail.objects.filter(lawyer_id = lawyer.id).order_by('-tran_date')
        duedates = AppDueDate.objects.filter(matter__handling_lawyer_id = lawyer.id, date_complied = None).order_by('duedate')

    except Lawyer_Data.DoesNotExist:
        lawyer = None
        matters = None
        tasks = None
        duedates = None
    
    context = {
        'user' : user,
        'matters': matters,
        'lawyer' : lawyer,
        'tasks' : tasks,
        'duedates': duedates,
    }
    if user.rank == 'ASSOCIATES':
        return render(request, 'user/user_detail_lawyer.html', context)  
    else:
        return render(request, 'user/user_detail.html', context)


def userloginview(request):
    form = userloginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            email = user.email
            print(email)
            if user is not None:
                send_otp(request)
                request.session['username'] = username
                return redirect('otp')
            else:
                return redirect('login')
    
    context = {
        'form' : form,
    }

    return render(request, 'user/login.html', context)


def otp_view(request):
    form = OTPForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            otp = form.cleaned_data['otp']
            username = request.session['username']
            otp_secret_key = request.session['otp_secret_key']
            otp_valid_until = request.session['otp_valid_date']

            if otp_secret_key and otp_valid_until:
                valid_until = datetime.fromisoformat(otp_valid_until)
                if valid_until > datetime.now():
                    totp = pyotp.TOTP(otp_secret_key, interval=60)
                    if totp.verify(otp):
                        user = get_object_or_404(User, username=username)
                        login(request, user)
                        del request.session['otp_secret_key']
                        del request.session['otp_valid_date']
                        return redirect('dashboard-index')
                    else:
                        error_message = 'Invalid one-time password'
                        return redirect('login')
                else:
                    error_message = "One-time password has expired"
                    return redirect('login')
            else:
                error_message = "Oopps.. something went wrong"
                return redirect('login')
        else:
            return redirect('login')
            
        # if error_message:messages.add_message(request, messages.ERROR, error_message)

    context = {
        'form': form,
    }

    return render(request, 'user/otp.html', context)

                

