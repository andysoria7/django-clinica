from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def mostar(request):
    return HttpResponse("<h2> Bievenidos! Esto es Checked Code </h2>")

def mostarDateTime(request):
    dt = datetime.datetime.now()
    dt = str(dt)
    c = "<h2> Fecha y hora actual: </h2>" + "<b>" + dt + "</b>"
    return HttpResponse(c)
