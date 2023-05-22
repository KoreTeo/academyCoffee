from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

"""
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()

    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)
"""


def cart(request):
    return render(request, 'main/cart.html')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def personalaccount(request):
    return render(request, 'main/personalaccount.html')


def stocks(request):
    return render(request, 'main/stocks.html')


def menu(request):
    return render(request, 'main/menu.html')