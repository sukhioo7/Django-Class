from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('<int:page>/',views.home,name='patient_home'),
    path('contact/',views.contact,name='contact'),
    path('delete/<int:id>/',views.delete,name='delete_patient'),
    path('update/<int:id>/',views.update,name='update_patient'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('filter/<str:gender>/',views.filter,name='filter_patient')
]
# www.hospial.com/patient/