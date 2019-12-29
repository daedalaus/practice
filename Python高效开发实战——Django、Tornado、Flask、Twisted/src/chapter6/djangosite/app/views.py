import os
import datetime
from app.forms import MomentForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import HttpResponse, render


def welcome(request):
    return HttpResponse('<h1>Welcome to my tiny twitter!</h1>')


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse('first-url'))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates',
                                        'moments_input.html'), {'form': form})


def current_datetime(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(now)


def my_404(request):
    return HttpResponse(status=404)


def my_404_2(request):
    return HttpResponseNotFound()
