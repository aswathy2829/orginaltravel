from django.shortcuts import render
from . models import Place
from . models import Team

from django.http import HttpResponse


def index(request):
    obj=Place.objects.all()
    return render(request, 'index.html',{'result':obj})

def index(request):
    obj1=Team.objects.all()
    return render(request, 'index.html',{'result1':obj1})
def elements(request):
    return render(request, 'elements.html')


def destinations(request):
    return render(request, 'destinations.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')
