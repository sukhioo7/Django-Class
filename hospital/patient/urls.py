from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('',views.home,name='patient_home'),
    path('contact/',views.contact,name='contact'),
    path('delete/<int:id>/',views.delete,name='delete_patient')
]
# www.hospial.com/patient/