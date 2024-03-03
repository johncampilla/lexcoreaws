from django.urls import path
from . import views

urlpatterns = [
    path('invoice/', views.InvoiceList, name='invoice-index'),
    path('invoice/newinvoice/', views.NewInvoice, name='new-invoice'),
    path("invoice/editinvoice/<int:pk>/'", views.EditInvoice, name='edit-invoice'),
    path("invoice/viewinvoice/<int:pk>/'", views.ViewInvoice, name='view-invoice'),
    path("invoice/invimages/<int:pk>/'", views.ViewInvoiceImage, name='view-invoice-image'),
    path('invoice/invmatters/', views.prepareinvoice, name='list-allmatters'),
    path("invoice/tempbill/<int:pk>/'", views.tobillmatter, name='invoice-matter'),

    path('invoice/newPF/', views.NewTempPf, name='invoice-newPF'),
    path("invoice/editPF/<int:pk>/'", views.EditTempPf, name='invoice-editPF'),
    path("invoice/deletePF/<int:pk>/'", views.RemoveTempPf, name='invoice-deletePF'),

    path('invoice/newFees/', views.NewTempFees, name='invoice-newFees'),
    path("invoice/editfees/<int:pk>/'", views.EditTempFees, name='invoice-editfees'),
    path("invoice/deleteFees/<int:pk>/'", views.RemoveTempfees, name='invoice-deletefees'),

]