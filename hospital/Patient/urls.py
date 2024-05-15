from django.urls import path
from . import views

app_name = 'Patient'

urlpatterns = [
    path('',views.patient,name='patient_page')
]