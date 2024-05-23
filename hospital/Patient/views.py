from django.shortcuts import render,HttpResponse
from . import models
from django.db import IntegrityError

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


def delete_patient(request,id):
    patient = models.Patient.objects.get(patient_id=id)
    patient.delete()
    return HttpResponse('Patient Delete ')