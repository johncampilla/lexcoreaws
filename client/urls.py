from django.urls import path
from . import views

urlpatterns = [
    path("client/", views.ClientList, name='client-index'),
    path("client/selectclient/<int:pk>/'", views.SelectClient, name='select-client'),
    path("client/newclient/", views.newclient, name='new-client'),
    path("client/viewfoldermatters/<int:pk>/<int:cid>/'", views.viewfoldercount, name='folder-matters'),
    path("client/newclientmatter/<int:pk>/'", views.newclient_matter, name='newclient-matter'),
    path("client/editclientmatter/<int:pk>/<int:cid>/'", views.editclientmatter, name='editclient-matter'),
    path("client/removeclientmatter/<int:pk>/<int:cid>/'", views.removeclientmatter, name='removeclient-matter'),
    
    path("client/newfolder/", views.newfolder, name='newclient-folder'),
    path("client/newfoldermatter/<int:pk>/<int:cid>/'", views.newfoldermatter, name='newfolder-matter'),
    
    path("client/selectfolder/<int:pk>/<int:cid>/'", views.selectfolder, name='select-folder'),
    


    path("client/editclient/<int:pk>/'", views.editclient, name='edit-client'),
    path("client/removeclient/<int:pk>/'", views.removeclient, name='remove-client'),

    path("client/newcontacts/", views.newcontactperson, name='new-contact'),
    path("client/editcontacts/<int:pk>/<int:cid>/'", views.editclientcontact, name='edit-contact'),
    path("client/viewcontactdetails/<int:pk>/<int:cid>/<str:contacts>/'", views.viewconnectedclients, name='viewclientdetails-contact'),
    path("client/viewconnectedmatterdetails/<int:pk>/<int:cid>/<str:contacts>/'", views.viewconnectedmatters, name='viewmatterdetails-contact'),

    path("client/deletecontact/<int:pk>/<int:cid>/'", views.removecontact, name='remove-contact'),
   
]    
