from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>hire me :) - zhaire</h1>")

def v1(response):
    return HttpResponse("<h1>view 1")    

# Create your views here.
