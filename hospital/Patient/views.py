from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.db import IntegrityError
from django.db.models import Q 
from django.contrib import messages
import pandas as pd


# Create your views here.
def patient(request):
    if request.GET:
        query = request.GET['search']
        patients = models.Patient.objects.filter(Q(patient_name__icontains=query) 
        | Q(patient_email__icontains=query) | Q(patient_phone__icontains=query)
        | Q(patient_symptoms__icontains=query)).all()
        data = {
            'patients':patients
        }
        return render(request,'Patient/patient.html',context=data) 

    if request.POST:
        full_name = request.POST['full_name']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        symptoms = request.POST['symptoms']

        if all([full_name,age,phone,email,gender,city,symptoms]): 
            if request.FILES.get('image'):
                image = request.FILES['image']
                try:
                    patient = models.Patient()
                    patient.patient_name = full_name
                    patient.patient_age = age
                    patient.patient_phone = phone
                    patient.patient_email = email
                    patient.patient_city = city
                    patient.patient_gender = gender
                    patient.patient_symptoms = symptoms
                    patient.patient_image = image
                    patient.save()
                    
                    return render(request,'home.html',context={'success':'done'})
                except IntegrityError as e:
                    if 'patient_email' in str(e):
                        error = {
                            'error':'email-error'
                        }
                    elif 'patient_phone' in str(e):
                        error = {
                            'error':'phone-error'
                        }
                    else:
                        error = {
                            'error':'else'
                        }
            else:
                error = {
                    'error':'empty-image'
                }
        else:
            error = {
                'error':'empty-fields'
            }
        return render(request,'home.html',context=error)
    # 'select * from patients;'
    patients = models.Patient.objects.all()

    data = {
        'patients':patients
    }
    return render(request,'Patient/patient.html',context=data) 

def filter_patient(request,by):
    if by=='male':
        patients = models.Patient.objects.filter(patient_gender="Male").all()
        data = {
            'patients':patients
        }
    elif by=='female':
        patients = models.Patient.objects.filter(patient_gender="Female").all()
        data = {
            'patients':patients
        }
    elif by=='age-asc':
        patients = models.Patient.objects.order_by('patient_age')
        data = {
            'patients':patients
        }
    elif by=='age-desc':
        patients = models.Patient.objects.order_by('-patient_age')
        data = {
            'patients':patients
        }
    return render(request,'Patient/patient.html',context=data)
    

def convert2excel(request):
    patients = models.Patient.objects.all().values(
                        'patient_id','patient_name','patient_age','patient_phone',
                        'patient_email','patient_gender','patient_city','patient_symptoms',
                        'registered_time')
    
    columns = ['ID','Name','Age','Phone','Email','Gender','City','Symptoms','Registered Date']

    raw = pd.DataFrame(patients)
    raw.columns = columns
    raw.to_excel('patient.xlsx')
    return redirect('Patient:patient_page')


def delete_patient(request,id):
    patient = models.Patient.objects.get(patient_id=id)
    patient.patient_image.delete()
    patient.delete()
    return redirect('Patient:patient_page')


def update(request,id):
    if request.POST:
        full_name = request.POST['full_name']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        symptoms = request.POST['symptoms']

        if all([full_name,age,phone,email,gender,city,symptoms]): 

                try:
                    patient = models.Patient.objects.get(patient_id=id)
                    patient.patient_name = full_name
                    patient.patient_age = age
                    patient.patient_phone = phone
                    patient.patient_email = email
                    patient.patient_city = city
                    patient.patient_gender = gender
                    patient.patient_symptoms = symptoms
                    if request.FILES.get('image'):
                        patient.patient_image.delete()
                        patient.patient_image = request.FILES.get('image')
                    patient.save()
                    
                    return render(request,'Patient/update.html',context={'success':'done','patient':patient})
                except IntegrityError as e:
                    if 'patient_email' in str(e):
                        error = {
                            'error':'email-error'
                        }
                    elif 'patient_phone' in str(e):
                        error = {
                            'error':'phone-error'
                        }
                    else:
                        error = {
                            'error':'else'
                        }
        else:
            error = {
                'error':'empty-fields'
            }
        error['patient'] = patient
        return render(request,'Patient/update.html',context=error)
    patient = models.Patient.objects.get(patient_id=id)
    data = {'patient':patient}
    return render(request,'Patient/update.html',context=data)