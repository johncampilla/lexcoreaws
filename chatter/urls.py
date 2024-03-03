from django.urls import path
from . import views


urlpatterns = [
    path("chatter/inboxchat", views.index, name='chatter-box'),
    path("chatter/sentchatitems", views.sentchatbox, name='chatter-sentbox'),
    path("chatter/notify/", views.notify_chat, name='unread_messages'),
    path("chatter/chat/", views.send_chat, name='send-chat'),
    path("chatter/openchat/<int:pk>/'", views.openchat, name='open-chat'),
    path("chatter/reviewchat/<int:pk>/'", views.reviewchat, name='view-chat'),

    
]