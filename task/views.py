from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html', {'task_list':Task.objects.all()})

def create(request):
    if request.method=='POST':
        text = request.POST['text']
        text_obj = Task(text=text)
        text_obj.save()
    return redirect("index")

def update(request, id):
    text_obj = Task.objects.get(id=id)
    if request.method=='POST':
        new_text = request.POST['text']
        text_obj.text = new_text
        text_obj.save()
    return redirect("index")

def delete(request, id):
    text_obj = Task.objects.get(id=id)
    if request.method=='POST':
        text_obj.delete()
    return redirect("index")

