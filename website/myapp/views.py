from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    task = Task.objects.order_by('id')
    return render(request, 'myapp/index.html', {'title': 'Главная страница', 'tasks': task})

def about(request):
    return render(request, 'myapp/aboutus.html', {'title': 'О нас'})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной."
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'myapp/create.html', {'title': 'Создать задачу'})