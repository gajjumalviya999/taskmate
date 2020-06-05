from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tasklist
from .forms import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import  login_required 
# Create your views here.
@login_required
def todolist(request):
    if request.method =="POST":
        form = taskform(request.POST or None)
        if form.is_valid():

            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
            messages.success(request,("new task added"))
            return redirect('todolist')
    else:
        all_task=tasklist.objects.filter(manage=request.user)
        paginator = Paginator( all_task , 5)
        page=request.GET.get('pg')
        all_task=paginator.get_page(page)
        return render(request,'todolist.html',{'all_task':all_task})

def delete_task(request,id):
    if manage.user==request.user:
        task=tasklist.objects.get(pk=id)
        task.delete()
       
    else:
        messages.error(request,"task cant be updated access denied")
    return redirect('todolist')
def edit_task(request,id):
    if request.method=="POST":

        task=tasklist.objects.get(pk=id)
        form=taskform(request.POST or None ,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"task updated")
        return redirect('todolist')
    else:
        task_obj=tasklist.objects.get(pk=id)
        return render(request,'edit.html',{'task_obj':task_obj})

def complete_task(request,id):
    task=tasklist.objects.get(pk=id)
    if manage.user==request.user:

        if task.done:
            task.done=False
        else :
            task.done=True
        task.save()  
    else:

        messages.error(request,"task cant be updated access denied")    
    return redirect('todolist')
    
def index(request):
    return render(request,'index.html',{'index_TEXT':"HII WELCOME to taskmate"})

def contact(request):
    return render(request,'contact.html',{'WELCOME_TEXT':"HII Welcome  contact"})
def about(request):
    return render(request,'about.html',{'WELCOME_TEXT':"HII WELCOME about"})