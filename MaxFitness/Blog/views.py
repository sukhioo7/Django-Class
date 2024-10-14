from django.shortcuts import render,HttpResponse

# Create your views here.

def blog_home(request):
    return render(request, 'Blog/home.html')
