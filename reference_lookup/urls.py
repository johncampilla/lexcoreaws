from django.urls import path
from . import views

urlpatterns = [
    path("reference/", views.index, name='reference-index'),

    path("lookup/newtaskcode/", views.NewTaskCode, name='new-taskcode'),
    path('lookup/edittaskcode/<int:pk>/', views.EditTaskCode, name='edit-taskcode'),

    path("lookup/newduecode/", views.NewDueCode, name='new-duecode'),
    path('lookup/editduecode/<int:pk>/', views.EditDueCode, name='edit-duecode'),
    path('lookup/removeduecode/<int:pk>/', views.RemoveDueCode, name='remove-duecode'),


    path('lookup/definefilingfees/<int:pk>/', views.definefilingfees, name='define-fees'),
    path("lookup/addfilingfee/", views.addfees, name='add-fees'),

    path('lookup/removetaskcode/<int:pk>/', views.RemoveTaskCode, name='remove-taskcode'),
    
    path("newindustry/", views.newIndustryCode, name='new-industry'),
    path("lookup/currency/codes", views.NewCurrencyCode, name='newcurrency'),


    path("editindustry/<int:pk>/'", views.EditIndustryCode, name='edit-industry'),
    path("editcurrency/<int:pk>/'", views.EditCurrencyCode, name='edit-currency'),
    path("removecurrency/<int:pk>/'", views.RemoveCurrencyCode, name='remove-currency'),

    path("lookup/removeindustry/<int:pk>/'", views.RemoveIndustryCode, name='remove-industry'),

    path("newapptype/", views.NewAppType, name='new-apptype'),
    path("editapptype/<int:pk>/'", views.EditAppType, name='edit-apptype'),
    path("lookup/removeapptype/<int:pk>/'", views.RemoveAppType, name='remove-apptype'),

    path("newfoldertype/", views.NewFolderType, name='new-foldertype'),
    path("editfolder/<int:pk>/'", views.EditFolderType, name='edit-folder'),
    path("lookup/removefolder/<int:pk>/'", views.RemoveFolderType, name='remove-folder'),
    
    path("newcasetype/", views.NewCaseType, name='new-casetype'),
    path("editcasetype/<int:pk>/'", views.EditCaseType, name='edit-casetype'),
    path("lookup/removecasetype/<int:pk>/'", views.RemoveCaseType, name='remove-casetype'),

    path("newnature/", views.NewNature, name='new-nature'),
    path("editnature/<int:pk>/'", views.EditNature, name='edit-nature'),
    path("lookup/removenature/<int:pk>/'", views.RemoveNature, name='remove-nature'),
    
    path("lookup/newactivitygroup/", views.StageGroup, name='new-activitygroup'),
    path("lookup/removestagegroup/<int:pk>/'", views.RemoveStageGroup, name='remove-stagegroup'),
    path("editstagegroup/<int:pk>/'", views.EditStageGroup, name='edit-stagegroup'),

    path("casestatus/", views.CaseStatus, name='new-status'),
    path("lookup/removestatus/<int:pk>/'", views.RemoveCaseStatus, name='remove-status'),
    path("editstatus/<int:pk>/'", views.EditCaseStatus, name='edit-status'),
    



    path("newapperance/", views.NewAppearance, name='new-appearance'),
    path("editappearance/<int:pk>/'", views.EditAppearance, name='edit-appearance'),
    path("lookup/removeappearance/<int:pk>/'", views.RemoveAppearance, name='remove-appearance'),
    
    path("newcourts/", views.NewCourts, name='new-courts'),
    path("editcourts/<int:pk>/'", views.EditCourts, name='edit-courts'),
    path("lookup/removecourts/<int:pk>/'", views.RemoveCourts, name='remove-courts'),

]
