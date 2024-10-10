from django.urls import path
from . import views


urlpatterns = [
    path('',views.application_home)
]

# www.amazon.com/