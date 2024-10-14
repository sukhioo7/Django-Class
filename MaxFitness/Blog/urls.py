from django.urls import path
from . import views

# www.maxfit.com/blog/

urlpatterns = [
    path('',views.blog_home,name='blog_app')
]