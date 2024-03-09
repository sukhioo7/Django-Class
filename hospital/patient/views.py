from django.shortcuts import render,HttpResponse,redirect
from . import models
import os
from django.db.models import Q
from django.contrib.auth.models import User
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

def update(request,id):
    patient = models.Patients.objects.filter(patient_id=id).get()
    if request.POST:
        full_name = request.POST['full_name'] 
        age = request.POST['age'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        city = request.POST['city'] 
        gender = request.POST.get('gender') 
        symptoms = request.POST['symptoms'] 
        if all([full_name,age,email,phone,city,gender,symptoms]):
            patient.patient_name = full_name
            patient.patient_age = age
            patient.patient_city = city
            patient.patient_email = email
            patient.patient_phone = phone
            patient.patient_gender = gender
            patient.patient_symptoms = symptoms
            patient.save()
            return redirect('patient:patient_home')
        else:
            error = {
                'empty_values':True,
                'patient':patient
            }
        return render(request,'patient/update.html',context=error)
    data = {
        'patient':patient
    }
    return render(request,'patient/update.html',context=data)

def login(request):
    return render(request,'patient/login.html')

def signup(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if all([first_name,last_name,username,email,password,confirm_password]):
            check_username = User.objects.filter(username=username).exists()
            check_email = User.objects.filter(email=email).exists()
            if not(check_username):
                if not(check_email):
                    if password==confirm_password:
                        user = User.objects.create(username=username,
                                                password=password,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                        user.is_active = True
                        user.save()
                        msg = {
                            'account_created':True
                        }
                    else:
                        msg = {
                            'password_error':True
                        }   
                else:
                    msg = {
                        'email_exist':True
                    }
            else:
                msg = {
                    'username_exist':True
                }
        else:
            msg = {
                'empty_values':True
            }
        return render(request,'patient/signup.html',context=msg)
    return render(request,'patient/signup.html')