from django.urls import path
from . import views

urlpatterns = [
    # path('activity/', views.DocketingListView, name='task-list'),
    path('activity/', views.matterlist, name='task-list'),
    path("activity/add/<int:mid>/'", views.NewActivity, name='new-activity'),
    path("activity/del/<int:pk>/'", views.RemoveActivity, name='delete-activity'),
    path("activity/edit/<int:pk>/'", views.EditActivity, name='edit-activity'),
    #2/21/2023
    path("activity/viewactivity/<int:pk>/<int:mid>/'", views.ViewActivity, name='view-activity'),
    path("activity/viewattachdocs/<int:pk>/'", views.viewattachdocument,  name='view-attach'),



    path("activity/newoutgoing/", views.NewOutgoingActivity, name='outgoing'),
    path("activity/newincoming/", views.NewIncomingActivity, name='incoming'),
    path("activity/selectactivity/<int:pk>/'", views.SelectedActivity, name='select-activity'),
    path("activity/edittempbill/<int:pk>/'", views.edittempbills, name='edit-tempbills'),
    path("activity/removetempbill/<int:pk>/'", views.removetembills, name='remove-tempbills'),

    path("activity/edittempfees/<int:pk>/'", views.edittempfees, name='edit-tempfees'),

]