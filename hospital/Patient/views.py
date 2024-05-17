from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.
def patient(request):
    if request.POST:
        full_name = request.POST['full_name']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        symptoms = request.POST['symptoms']

        if all([full_name,age,phone,email,gender,city,symptoms]):
            patient = models.Patient()
            patient.patient_name = full_name
            patient.patient_age = age
            patient.patient_phone = phone
            patient.patient_email = email
            patient.patient_city = city
            patient.patient_gender = gender
            patient.patient_symptoms = symptoms
            patient.save()

    return render(request,'Patient/patient.html') 