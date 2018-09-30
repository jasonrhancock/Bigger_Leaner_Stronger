from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import datetime

def index(request):
    template = loader.get_template('workouts/workout_template.html')
    context = {"some_text": "Hello, world. You're at the polls index."}
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(template.render(context, request))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
