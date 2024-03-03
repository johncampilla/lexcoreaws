from django.shortcuts import render, redirect
from .models import inboxmessage, tempchatmessages
from matter.models import Matters, IP_Matter
from emailportal.models import Emails
from userprofile.models import User_Profile
from django.contrib.auth.models import User
from .forms import chatform
from django.contrib.auth.decorators import login_required 

# Create your views here.
# all messages address to the user
@login_required
def index(request):
    access_code = request.user.user_profile.userid
    fromuser = request.user
    
    msginbox = inboxmessage.objects.filter(messageto__userid=access_code)
    inboxcount = msginbox.count() 

    # msgsent = inboxmessage.objects.filter(messagefrom = fromuser)
    # sentcount = msgsent.count() 
    form = chatform() 

    context = {
        'msginbox' : msginbox,
#        'sentmsg' : msgsent,
        'form' : form,
    }
    return render(request, 'chatter/mychatbox.html', context)

# all messages sent by the users
@login_required
def sentchatbox(request):
    fromuser = request.user
    msgsent = inboxmessage.objects.filter(messagefrom = fromuser)
    form = chatform() 

    context = {
        'msgsent' : msgsent,
        'form' : form,
    }
    return render(request, 'chatter/mysentbox.html', context)

@login_required
def notify_chat(request):
    user_message_id = request.user.user_profile.id
    chatmessages = inboxmessage.objects.filter(
        messageto_id=user_message_id, status="UNREAD")
    
    form = chatform


    context = {
        'chatmessages': chatmessages,
        'form' : form,
    }

    return render(request, 'chatter/unreadmessages.html', context)

@login_required
def reviewchat(request, pk):
    user_message_id = request.user.user_profile.id
    fromuser = request.user
    message = inboxmessage.objects.get(id = pk)
    msgfrom = message.messagefrom
    message_from = message.messagefrom
    msg_id_messages = inboxmessage.objects.filter(messagefrom = msgfrom)
    tempchatmessages.objects.all().delete()
    form = chatform

    for data in msg_id_messages:
        if data.messageto_id == user_message_id:
            messageto = data.messageto
            messagefrom = data.messagefrom
            messagebox = data.messagebox
            messagedate = data.created_at
            status = data.status
            see_matter = data.see_matter
            messagerec = tempchatmessages(messageto = messageto, messagefrom = messagefrom, messagedate = messagedate, messagebox = messagebox,status = status, see_matter=see_matter)
            messagerec.save()

    msgfrom = request.user
    msg_id_messages = inboxmessage.objects.filter(messagefrom = msgfrom)
    msgto = User_Profile.objects.get(userid__username = message_from)
    for data in msg_id_messages:
        if data.messageto_id == msgto.id :
            messageto = data.messageto
            messagefrom = data.messagefrom
            messagebox = data.messagebox
            messagedate = data.created_at
            status = data.status
            see_matter = data.see_matter
            messagerec = tempchatmessages(messageto = messageto, messagefrom = messagefrom, messagedate = messagedate, messagebox = messagebox,status = status, see_matter=see_matter)
            messagerec.save()
    
    msginbox = tempchatmessages.objects.all().order_by('messagedate')
    
    context = {
        'msginbox' : msginbox, 
        'form': form,
    }

    return render(request, 'chatter/viewchat.html', context)
    
@login_required
def send_chat(request):
    if request.method == 'POST':
        form = chatform(request.POST)
        if form.is_valid():
            chat_rec = form.save(commit=False)
            chat_rec.messagefrom = request.user
            chat_rec.status = 'UNREAD'
            chat_rec.save()                 
            return redirect('chatter-box')        
        else:
            form = chatform()
    else:
        form = chatform()

@login_required
def openchat(request, pk):
    chat = inboxmessage.objects.get(id = pk)
    matter = Matters.objects.get(id = chat.see_matter_id)
    emails = Emails.objects.filter(matter_id = matter.id).order_by('-created_at')
    mattermessages = inboxmessage.objects.filter(see_matter_id = matter.id).order_by('-created_at')
    try:
        ip_matter = IP_Matter.objects.get(id=chat.see_matter_id)
    except IP_Matter.DoesNotExist:
        ip_matter = None    
        
    chat.status = 'READ'
    chat.save()

    context = {
        'message' : chat,
        'matter' : matter,
        'ip_matter': ip_matter,
        'msginbox' : mattermessages,
        'emails' : emails,
    }
    return render(request, 'chatter/chatdetail.html', context)

