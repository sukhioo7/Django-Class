from django.shortcuts import render,HttpResponse

# Create your views here.

def application_home(request):
    return HttpResponse('This is the home page of the application.')
