from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    if request.POST:
        full_name = request.POST['full_name'] 
        age = request.POST['age'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        city = request.POST['city'] 
        gender = request.POST['gender'] 
        symptoms = request.POST['symptoms'] 

        patient = models.Patients()
        patient.patient_name = full_name
        patient.patient_age = age
        patient.patient_city = city
        patient.patient_email = email
        patient.patient_phone = phone
        patient.patient_gender = gender
        patient.patient_symptoms = symptoms
        patient.save()

        return render(request,'patient/success.html')
    else:
        # select * from patients;
        patients = models.Patients.objects.all()
        data = {
            'patients':patients
        }
        return render(request,'patient/home.html',context=data)


def contact(request):
    return render(request,'patient/contact.html')
