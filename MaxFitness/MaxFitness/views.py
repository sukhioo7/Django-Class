from django.shortcuts import render
from Blog.models import Blog


def home(request):
    blogs = Blog.objects.all().order_by('post_date')
    data = {
        'blogs': blogs
    }
    return render(request, 'home.html',context=data)