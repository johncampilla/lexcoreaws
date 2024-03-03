from django.urls import path
from . import views
from .views import dashchart, chart_data

urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('dashboard/details/newmatters', views.details_new_matters, name='dashboard-details-newmatters'),
    path('dashboard/details/newclients', views.details_new_clients, name='dashboard-details-newclients'),
    path('dashboard/details/newbills', views.details_newbills, name='dashboard-details-newbills'),
    path('dashboard/details/newcertificates', views.details_ip_issuance, name='dashboard-details-issuance'),
    path('dashboard/newtask/', views.newactivity, name='dashboard-addtask'),  
    path('dashboard/searchlist', views.searchlist, name='dashboard-searchlist'),
    path('dashboard/totalindustry/', views.totalcountindustry, name='chart-totalindustry'),
    path('dashboard/totalapptype/', views.totalcountapptype, name='chart-totalapptype'),
    path('dashboard/totallawyers/', views.totalcountlawyers, name='chart-totallawyers'),
    path('dashboard/totalfolders/', views.totalcasefolders, name='chart-totalfolders'),
    path('dashboard/totalcasetype/', views.totalcasetype, name='chart-totalcasetype'),
    path('dashboard/totalnature/', views.totalnature, name='chart-totalnature'),
    path('dashboard/printapptype/', views.printapptypecount, name='chart-print-apptype'),
    path('dashboard/printindustry/', views.printindustrycount, name='chart-print-industry'),
    path('dashboard/printlawyer/', views.printlawyercount, name='chart-print-lawyer'),
    path('dashboard/printfolder/', views.printfoldercount, name='chart-print-folder'),
    path('dashboard/printcasetype/', views.printcasetypecount, name='chart-print-casetype'),
    path('dashboard/printnature/', views.printnaturecount, name='chart-print-nature'),

    path('dashboard/reports/', views.reports, name='reports-items'),
    path("dashboard/reports/group/<int:pk>'/", views.selectreportgroup, name='reports-group'),
    path("dashboard/reports/selectedreport/<int:pk>'/", views.selectedreport, name='report-selected'),
    path("dashboard/pdf/selectedreport1/<int:pk>'/", views.client_report_1_pdf_view, name='pdf-client_report_1'),
    path("dashboard/pdf/selectedreport2/<int:pk>'/", views.client_report_2_pdf_view, name='pdf-client_report_2'),
    path("dashboard/pdf/selectedreport3/<int:pk>'/", views.client_report_3_pdf_view, name='pdf-client_report_3'),
    path("dashboard/pdf/selectedreport4/<int:pk>'/", views.client_report_4_pdf_view, name='pdf-client_report_4'),

#new set of dashboard

    # path('', dashchart.as_view(), name='dashboard-chart'),
    # path('chart-data/', chart_data, name='data'),



    # detail of summary
    path("dashboard/printlist/<str:selected>/'", views.detailapplicationtype, name='print-selected-apptype'),
    path("dashboard/printlist_industry/<str:selected>/'", views.detailindustry, name='print-selected-industry'),
    path("dashboard/printlist_lawyers/<str:selected>/'", views.detaillawyers, name='print-selected-lawyers'),
    path("dashboard/printlist_folders/<str:selected>/'", views.detailfolders, name='print-selected-folders'),
    path("dashboard/printlist_casetype/<str:selected>/'", views.detailcasetype, name='print-selected-casetype'),
    path("dashboard/printlist_nature/<str:selected>/'", views.detailnature, name='print-selected-nature'),





    
]
