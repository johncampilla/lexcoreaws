from django.urls import path
from . import views


urlpatterns = [
    path('matter/', views.MatterList, name='matter-list'),
    path("matter/select/<int:pk>/'", views.SelectMatter, name='select-matter'),
    path('matter/newmatter/', views.NewMatter, name='new-matter'),
    path("matter/editmatter/<int:pk>'",views.EditMatter, name ='edit-matter'),
    path("matter/edit_ipmatter/<int:pk>'",views.Edit_IPMatter, name ='edit-ipmatter'),
    path('matter/priority/', views.NewPriority_modal, name='matter-new-priority'),
    path("matter/editpriority/<int:pk>/<int:mid>/'", views.EditPriority, name='matter-editpriority'),
    path("matter/viewactivity/<int:pk>/<int:mid>/'", views.ViewActivity, name='matter-viewactivity'),
    path("matter/attachdocs/<int:pk>/'", views.AttachDocument, name='matter-attachdocument'),

    path("matter/viewattachdocs/<int:pk>/'", views.viewattachdocument,  name='matter-viewattach'),



    path("matter/editactivity/<int:pk>/<int:mid>/'", views.EditActivity, name='matter-editactivity'),

    path("matter/deletepriority/<int:pk>/<int:mid>/'", views.RemoveMatterPriority, name='matter-deletepriority'),


    path('matter/newmatterinfo/', views.NewMatterInfo, name='new-matterinfo'),
    path('matter/newfolder/', views.newfolder, name='matter-new-folder'),    


# Due Date Tab functions
    path("matter/duedate/select/<int:pk>/<int:mid>/'", views.EditDueDate, name='edit-duedate'),
    path("matter/duedate/del/<int:pk>/<int:mid>/'", views.RemoveDueDate, name='delete-duedate'),
    path("matter/duedate/select/<int:pk>/<int:mid>/'", views.EditDueDate, name='edit-duedate'),
    path("matter/duedate/add/<int:mid>/'", views.NewDueDate, name='new-duedate'),

    path("matter/duedate/add", views.NewDueDateModal, name='new-duedateModal'),


# Applicant Tab functions
    path("matter/applicant/add/<int:mid>/'", views.NewApplicant, name='new-applicant'),
    path("matter/newapplicant/", views.NewApplicantModal, name='new-modalapplicant'),
    path("matter/matterapplicant/add/", views.NewMatterApplicant, name='new-matter-applicant'),
    path("matter/applicantlist/add/<int:mid>/'", views.NewApplicantProfile, name='new-applicantprofile'),
    path("matter/applicant/edit/<int:pk>/'", views.EditApplicant, name='edit-applicant'),
    path("matter/applicantmain/edit/<int:pk>/<int:mid>/'", views.EditMatterApplicant, name='edit-mainapplicant'),
    path("matter/viewapplicants/", views.viewapplicants, name='view-applicants'),
    path("matter/viewinventors/<int:mid>/'", views.viewinventors, name='view-inventors'),
    path("matter/newinventor/", views.NewInventorModal, name='new-modalinventor'),
    path("matter/matterinventor/add/", views.NewMatterInventor, name='new-matter-inventor'),

    path("matter/applicant/del/<int:pk>/<int:mid>/'", views.Delete_Applicant, name='delete-applicant'),
    path("matter/matterapplicant/del/<int:pk>/<int:mid>/'", views.Delete_MatterApplicant, name='delete-matterapplicant'),

    path("matter/addimage/<int:pk>/'", views.addimage, name='add-image'),
    path("matter/editimage/<int:pk>/'", views.editimage, name='edit-image'),
    path("matter/deleteimage/<int:pk>/'", views.deleteimage, name='delete-image'),


    # path("matter/casehistory/add/<int:mid>/'", views.NewCaseHistory, name='new-casehistory'),

# casedescription tab functions
    path("matter/casedescription/add/<int:mid>/'", views.NewCaseDescription, name='new-casedescription'),

# case_evidence tab functions
    path("matter/caseevidence/add/<int:mid>/'", views.NewCaseEvidence, name='new-case_evidence'),
    path("matter/evidence/view/<int:pk>/<int:mid>/'", views.ViewEvidence, name='view-case_evidence'),

# Priority
    path("matter/priority/add/<int:mid>/'", views.NewPriority, name='new-priority'),

# classOfGoods
    path("matter/classofgoods/add/", views.NewClassOfGoods, name='new-classofgoods'),
    path("matter/classofgoods/edit/<int:pk>/<int:mid>/'", views.EditClassOfGoods, name='edit-classofgoods'),
    path("matter/classofgoods/del/<int:pk>/<int:mid>/'", views.RemoveClassGoods, name='remove-classofgoods'),

    path("matter/classofgoods/list/", views.viewclassofgoods, name='list-classofgoods'),
    path("matter/classofgoods/save/", views.newclgoodsprofile, name='profile-classofgoods'),

#
    path("matter/activity/add/<int:mid>/'", views.NewActivity, name='new-activity'),

#email
    path("matter/viewemail/<int:pk>/'", views.view_email, name='view-email'),
    path("matter/emailattach/<int:pk>/'", views.viewattachemail, name='email-attach'),



# Other Information
#    path("otherinfo/<int:pk>/<str:casetype>/'", views.viewotherinfo, name='otherinfo-bycasetype'),


]
