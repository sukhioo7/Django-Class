from django.urls import path
from . import views

# www.maxfit.com/blog/

app_name = 'Blog'

urlpatterns = [
    path('',views.blog_home,name='blog_app'),
    path('blog-page/',views.view_blog,name='view_blog'),
    path('add-new-blog/',views.add_blog,name='add_new_blog')
]