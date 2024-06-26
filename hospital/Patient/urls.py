from django.urls import path
from . import views

app_name = 'Patient'

urlpatterns = [
    path('<int:page>/',views.patient,name='patient_page'),
    path('delete/<int:id>/',views.delete_patient,name='delete-card'),
    path('update/<int:id>/',views.update,name='update-patient'),
    path('filter/<slug:by>/',views.filter_patient,name='filter-patient'),
    path('export-to-xlsx/',views.convert2excel,name='to-excel'),
    path('download-file/',views.download_excel,name='download-excel'),
    path('signup/',views.staff_signup,name='signup'),
    path('login/',views.staff_login,name='login'),
    path('logout/',views.logout,name='logout'),
]