from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('',views.home,name='patient_home'),
    path('contact/',views.contact,name='contact')
]
# www.hospial.com/patient/