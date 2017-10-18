from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def detail(request, question_id):
    return HttpResponse("You're looking at question " + question_id)