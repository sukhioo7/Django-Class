from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse('Hello all Wellcome to my Website')

def about(request):
    return HttpResponse('About Page')

def contact(request):
    return HttpResponse('Contact Page')
