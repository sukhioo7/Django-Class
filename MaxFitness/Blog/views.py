from django.shortcuts import render,HttpResponse

# Create your views here.

def blog_home(request):
    return render(request, 'Blog/home.html')

def add_blog(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'Blog/add_blog.html')