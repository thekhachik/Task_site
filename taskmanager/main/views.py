from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# from django.http import HttpResponse


def about(request):
    return render(request, 'main/about.html')
    # return HttpResponse('<h3>Hello, World!</h3>')


def index(request):
    tasks = Task.objects.order_by('-id')
    context = {'title': 'Главная страница сайта', 'tasks':tasks}
    return render(request, 'main/index.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Формы не корректны'

    form = TaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)
