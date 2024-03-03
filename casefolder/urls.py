from django.urls import path
from . import views

urlpatterns = [
    path('folders/', views.folderlist, name='folder-index'),
    path("folder_details/<int:pk>/'", views.folderdetail, name='folder-detail'),
    path("modify_folder/<int:pk>/'", views.modify_folder, name='modify-folder'),
    path('new_folder/', views.newcasefolder, name='new-folder'),
    path("foldermatters/<int:pk>/'", views.selectedfolder, name='selected-folder'),
    path("matterlist/<int:pk>/'", views.folder_listmatters, name='list-foldermatters'),
    path('newmatter/', views.FolderNewMatter, name='new-foldermatter'),



]
