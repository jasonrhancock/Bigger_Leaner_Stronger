from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import datetime

def index(request):
    template = loader.get_template('workout_template.html')
    context = {"payload": "This text was generated from views.py and passed to workout_template.html"}
    return HttpResponse(template.render(context, request))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
