from django.shortcuts import HttpResponse


def welcome(request):
    return HttpResponse('<h1>Welcome to my tiny twitter!</h1>')
