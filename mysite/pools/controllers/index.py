from django.http import HttpResponse
from django.shortcuts import redirect, render
from pools.models import Feedback


def index(request):

    return render(request, 'index.html', {})


def about(request):
    return HttpResponse("My name is Mikhail")


def contacts(request):
    return HttpResponse("My contacts")

def products(request):
    return HttpResponse("Our products")

def reviews(request):
    return HttpResponse("Our reviews")