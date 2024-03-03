from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Emails, EmailAttachments
from chatter.models import inboxmessage
from matter.models import Matters, AppDueDate
from invoice.models import AccountsReceivable
from activity.models import task_detail
from .forms import EmailForm, NewEmailForm
from client.models import Contact_Person
from django.contrib.auth.models import User
from userprofile.models import User_Profile

from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.decorators import login_required 

@login_required
def email_list(request):
    pass

@login_required
def email_index(request):
    return render(request, 'emailportal/mailsindex.html')

@login_required
def view_email(request, pk):
    form = NewEmailForm()
    email = Emails.objects.get(id=pk)
    matter = Matters.objects.get(id=email.matter_id)
    emails = Emails.objects.filter(matter_id = matter.id).order_by('-created_at')
    mattermessages = inboxmessage.objects.filter(see_matter_id = matter.id).order_by('-created_at')
    duedates = AppDueDate.objects.filter(matter_id = email.matter_id)
    activities = task_detail.objects.filter(matter_id = email.matter_id)
    invoices = AccountsReceivable.objects.filter(matter_id = email.matter_id)
    
    
    context = {
        'email' : email,
        'emails': emails,
        'msginbox' : mattermessages,
        'matter': matter,
        'duedates': duedates,
        'activities':activities,
        'invoices': invoices,
        'form': form,
    }
    return render(request, 'emailportal/openemail.html', context)
    
@login_required
def email_sentitems(request):
    fromuser = request.user
    userprofile = User_Profile.objects.get(userid__username = fromuser)    
    emails = Emails.objects.filter(sentby_id = userprofile.userid_id).order_by('-created_at') 
    context = {
        'emails': emails,
    }
    return render(request, 'emailportal/mail_sentitems.html', context)

@login_required
def email_contacts(request):
    contacts = Contact_Person.objects.all().order_by('-client')
    context = {
        'contacts' : contacts,
    }
    return render(request, 'emailportal/mail_contacts.html', context)

@login_required
def send_email(request):

    if request.method == 'POST':
        
        form = NewEmailForm(request.POST)
        if form.is_valid():
            print('valid naman ang form')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            email = request.POST.get('email')
            from_email = settings.EMAIL_HOST_USER

            email = EmailMessage(subject, message, from_email, [email])
            email.content_subtype = 'html'

            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)
            email.send()

            mail_rec = form.save(commit=False)
            mail_rec.sentby_id = request.user.id
            mail_rec.save() 

            email_rec = EmailAttachments(email_id=mail_rec.id, emailattachment=file)
            email_rec.save()

            return redirect('my_sentitems')
            return HttpResponse("Sent")

        else:
            form = NewEmailForm()
    else:
        form = NewEmailForm()
    
    context = {
        'form' : form
    }

    return render(request, 'emailportal/composemail.html', context)

