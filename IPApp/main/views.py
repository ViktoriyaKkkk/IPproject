from django.shortcuts import render
from .models import Workers


def index(request):
    workersall = Workers.objects.order_by('surname')
    workerscount = Workers.objects.count()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'workersall': workersall,
                                               'workerscount': workerscount})


def about(request):
    workersall = Workers.objects.order_by('surname')
    return render(request, 'main/about.html', {'title': 'Главная страница сайта', 'workersall': workersall})


