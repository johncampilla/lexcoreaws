from django.urls import path
from . import views

urlpatterns = [
    path("templates/", views.templates, name='templates'),
    path("templates/docs/<int:pk>/'", views.doclist, name='docu-list'),
    path("templates/sampleprint/", views.sampleprint, name='docu-print'),

    path("templates/addtemplate/", views.addtemplate, name='newtemplate'),



]