from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def meghana(request):
    return HttpResponse('<h1>My name Is Meghanaaaa Sir!</h1>')

def srujana(request):
    return HttpResponse('<marquee><h1>Srujana Tinnava Ra, Era Vadilestunnavaa</h1></marquee>')