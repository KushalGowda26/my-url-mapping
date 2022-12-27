from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def banglore(request):
    return HttpResponse('<h1>today wheather in Banglore is little rainy and we have Django class at 12.00pm </h1>')

def tuesday(request):
    return HttpResponse('<h1>Successfully completed specific url mapping</h1>')