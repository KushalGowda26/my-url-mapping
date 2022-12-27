from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h2>This is my first request on 27th december 2022</h2>')

def second(request):
    return HttpResponse('<h2>This is my second request on 27th december 2022</h2>')
