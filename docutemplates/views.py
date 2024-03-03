from django.shortcuts import render, redirect
from .models import templatedocs
from .forms import *

# Create your views here.
def doclist(request, pk):
    docs = templatedocs.objects.filter(folder_id = pk).order_by('-created_at')
    context = {
        'docs':docs
    }
    if pk == 1:
        return render(request, 'docutemplates/IPTemplates.html', context)
    else:
        return render(request, 'docutemplates/doclist.html')
   
def sampleprint(request):
    return render(request, 'docutemplates/index.html')
    
def templates(request):
    templates = templatedocs.objects.all().order_by('-folder')
    context = {
        'templates' : templates
    }
    return render(request, 'docutemplates/doclist.html', context)

def addtemplate(request):
    if request.method == 'POST':
        form = TemplateForms(request.POST)
        if form.is_valid():
            fid = request.POST['folder']
            form.save()
            return redirect('docu-list', fid)
        else:
            form = TemplateForms()
    else:
        form = TemplateForms()
    
    context = {
        'form':form,
    }

    return render(request, 'docutemplates/newtemplate.html', context)



