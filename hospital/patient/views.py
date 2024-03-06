from django.shortcuts import render,HttpResponse,redirect
from . import models
import os
from django.db.models import Q

# Create your views here.

def home(request):
    if 'search' in request.POST:
        query = request.POST['query']
        patients = models.Patients.objects.filter(Q(patient_name__icontains=query) | Q(patient_age__icontains=query) | 
                                        Q(patient_city__icontains=query) | Q(patient_phone__icontains=query)
                                          | Q(patient_email__icontains=query)
                                        | Q(patient_symptoms__icontains=query))
    elif 'registration' in request.POST:
        full_name = request.POST['full_name'] 
        age = request.POST['age'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        city = request.POST['city'] 
        gender = request.POST.get('gender') 
        photo = request.FILES.get('photo')
        symptoms = request.POST['symptoms'] 
        if all([full_name,age,email,phone,city,gender,photo,symptoms]):
            check_email = models.Patients.objects.filter(patient_email=email).exists()
            check_phone = models.Patients.objects.filter(patient_phone=phone).exists()
            if not(check_email):
                if not(check_phone):
                    patient = models.Patients()
                    patient.patient_name = full_name
                    patient.patient_age = age
                    patient.patient_city = city
                    patient.patient_email = email
                    patient.patient_phone = phone
                    patient.patient_gender = gender
                    patient.patient_image = photo
                    patient.patient_symptoms = symptoms
                    patient.save()

                    return render(request,'patient/success.html')
                else:
                    error = {
                        'phone_exist' : True
                    }
            else:
                error = {
                    'email_exist' : True
                }
        else:
            error = {
                'empty_values':True
            }
        return render(request,'index.html',context=error)
    else:
        # select * from patients;
        patients = models.Patients.objects.all()
    data = {
        'patients':patients
    }
    return render(request,'patient/home.html',context=data)


def contact(request):
    return render(request,'patient/contact.html')

def delete(request,id):
    # select * from patients where patient_id=id;
    patient = models.Patients.objects.filter(patient_id=id).get()
    file_path = patient.patient_image.path
    os.remove(file_path)
    patient.delete()
    return redirect('patient:patient_home')