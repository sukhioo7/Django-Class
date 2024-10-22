from django.urls import path
from . import views

# www.maxfit.com/blog/

app_name = 'Blog'

urlpatterns = [
    path('',views.blog_home,name='blog_app'),
    path('blog-page/<int:blog_id>/',views.view_blog,name='view_blog'),
    path('add-new-blog/',views.add_blog,name='add_new_blog'),
    path('delete-blog/<int:blog_id>/',views.delete_blog,name='delete_blog')
]