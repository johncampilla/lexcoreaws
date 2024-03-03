from django.urls import path
from . import views

urlpatterns = [
    path("email_list/", views.email_index, name='my_emails'),
    path("email_sentitems/", views.email_sentitems, name='my_sentitems'),
    path("email_contacts/", views.email_contacts, name='my_contacts'),
    path("compose_email/", views.send_email, name='compose_email'),
    path("view_email/<int:pk>/'", views.view_email, name='view_email'),

]