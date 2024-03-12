from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import AppModel


def home(request):
    Users = AppModel.objects.all().values()
    context = {
        'users': Users
    }
    temp = loader.get_template('index.html').render(context, request)
    return HttpResponse(temp)

def details(request, id):
    """
    A bit of user details
    """
    User = AppModel.objects.get(id=id)
    context = {
        'users': User
    }
    temp = loader.get_template('details.html').render(context, request)
    return HttpResponse(temp)

def main(request):
    """
    default main page
    """
    temp = loader.get_template('base.html').render()
    return HttpResponse(temp)