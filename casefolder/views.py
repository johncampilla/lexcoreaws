from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CaseFolder, FolderType
from client.models import Contact_Person, Client_Data
from matter.models import Matters
from activity.models import task_detail
#from django.views.generic import ListView, FormView
from .forms import *
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q, Sum, Count
from django.contrib.auth.decorators import login_required 


import string
@login_required
def folderlist(request):
    folder_result = Matters.objects.values('folder__folder_type__id', 'folder__folder_type__folder').annotate(NoOfMatters=Count('matter_title'))
    folderlist = CaseFolder.objects.all().order_by('client__client_name', '-updated_at')
    
    #print(folder_result)
    #.filter(folder__client_id = pk).order_by('-NoOfMatters')
    form = NewCaseFolderForm()
    
    context = {
        'folders'       : folder_result,
        'folderlist'    : folderlist,
        'form'          : form,
    }
    return render(request, 'casefolder/foldercount.html', context)

@login_required
def folderdetail(request, pk):
    folder = CaseFolder.objects.get(id=pk)
    activities = task_detail.objects.filter(matter__folder_id = pk).order_by('-tran_date')
    #matters = folder.get_matters()
    matters = folder.folder_matters
    client = Client_Data.objects.get(id = folder.client_id)
    #matters = Matters.objects.filter(folder_id = pk)
    form = MatterForm

    
    context = {
        'folder' : folder,
        'matters': matters,
        'client' : client,
        'form'   : form,
        'activities': activities,

    }
    
    return render(request, 'casefolder/folder_detail.html', context)

@login_required
def selectedfolder(request, pk):
    matters = Matters.objects.filter(folder__folder_type__id = pk).order_by
    ('folder__client__client_name')
    folder = FolderType.objects.get(id=pk)
    context = {
        'matters':matters,
        'folder': folder,
    }

    return render(request, 'casefolder/matterlist.html', context)

@login_required
def folder_listmatters(request, pk):
    folder = CaseFolder.objects.get(id=pk)
    matters = Matters.objects.filter(folder_id = pk)
    clientname = folder.client.client_name
    form = MatterForm()

    context = {
        'folder' : folder,
        'matters' : matters,
        'clientname' : clientname,
        'form' : form,
    }
 
    return render(request, 'casefolder/folder_matterlist.html', context)

@login_required
def newcasefolder(request):
    if request.method == 'POST':
        form = CaseFolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('folder-index')


def modify_folder(request, pk):
    folder = CaseFolder.objects.get(id=pk)
    client = Client_Data.objects.get(id = folder.client_id)
    form = CaseFolderForm(request.POST, instance=folder)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('folder-detail', folder.id)
        else:
            form = CaseFolderForm(instance=folder)
    else:
        form = CaseFolderForm(instance=folder)
    
    context = {
        'form' : form,
        'folder': folder,
        'client': client,
    }

    return render(request, 'casefolder/editfolder.html', context)
            

        

@login_required
def FolderNewMatter(request):
    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            matter_rec = form.save(commit=False)
            matter_rec.folder_id = request.POST['folder']
            matter_rec.save()            
            return redirect('list-foldermatters', request.POST['folder'])











# Create your views here.
# class FolderListView(FormView, ListView):
#     template_name = 'casefolder/index.html'
#     context_object_name = 'folders'
#     ordering = '-created_at'
#     form_class = CaseFolderForm
#     # success_url = reverse_lazy('client:client-index')
#     def get_success_url(self):
#         return self.request.path

#     def get_queryset(self):
#         parameter = ''
#         return CaseFolder.objects.filter(folder_description__startswith=parameter).order_by('folder_type', 'client__client_name')

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     return context

#     def get_context_data(self):
#         # letters = list(string.ascii_uppercase)
#         # selected_letter = self.kwargs.get('letter') if self.kwargs.get('letter') else 'a'
#         context = {
#             'form':self.get_form_class(),
#             'folders': self.get_queryset(),
#         }
#         # print('selected_letter', selected_letter)
#         return context

#     def form_valid(self, form):
#         #form.save()
#         self.instance = form.save()
#         messages.add_message(self.request, messages.INFO, f"Case Folder: {self.instance.folder_description } has been created")
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         self.object_list = self.get_queryset()
#         messages.add_message(self.request, messages.ERROR, form.errors)

#         return super().form_invalid(form)
