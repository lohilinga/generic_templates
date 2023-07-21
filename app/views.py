from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def srujana(request):
    return HttpResponse('srujana tinnava raa....')
def meghana(request):
    return HttpResponse('<h1><marquee>my name is megana</marquee></h1>')
def lohi (request):
    return HttpResponse('<marquee><h1>helloworld</h1></marquee>')