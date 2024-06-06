from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.db import IntegrityError
from django.db.models import Q 
import pandas as pd
from django.conf import settings
import os
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def patient(request,page):
    if not(request.session.get('staff_id')):
        return redirect('Patient:login')
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
    paginator = Paginator(patients,5)
    pagination_patients = paginator.page(number=page)
    data = {
        'patients':pagination_patients
    }
    return render(request,'Patient/patient.html',context=data) 

def filter_patient(request,by):
    if not(request.session.get('staff_id')):
        return redirect('Patient:login')
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
    if not(request.session.get('staff_id')):
        return redirect('Patient:login')
    patients = models.Patient.objects.all().values(
                        'patient_id','patient_name','patient_age','patient_phone',
                        'patient_email','patient_gender','patient_city','patient_symptoms',
                        'registered_time')
    
    columns = ['ID','Name','Age','Phone','Email','Gender','City','Symptoms','Registered Date']

    raw = pd.DataFrame(patients)
    raw.columns = columns
    
    file_path = os.path.join(settings.MEDIA_ROOT,'files\patients.xlsx')

    raw.to_excel(file_path,index=False)

    return redirect('Patient:download-excel')

def download_excel(request):
    if not(request.session.get('staff_id')):
        return redirect('Patient:login')
    file_path = os.path.join(settings.MEDIA_ROOT, 'files\patients.xlsx')
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="patients.xlsx"'
            return response
    else:
        return HttpResponse('File not found')

def delete_patient(request,id):
    if not(request.session.get('staff_id')):
        return redirect('Patient:login')
    patient = models.Patient.objects.get(patient_id=id)
    patient.patient_image.delete()
    patient.delete()
    return redirect('Patient:patient_page',page=1)


def update(request,id):
    if not(request.session.get('staff_id')):
        return redirect('Patient:login')
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


def staff_signup(request):
    if request.POST:
        full_name = request.POST.get('full_name')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if all([full_name,designation,email,password,confirm_password]):
            if password==confirm_password:
                encriypt_password = make_password(password)
                try:
                    models.Staff.objects.create(staff_name=full_name,
                                                staff_designation=designation,
                                                staff_email=email,
                                                staff_password=encriypt_password)
                    return render(request,'Patient/signup.html',context={'success':'done'})
                except IntegrityError as e:
                    if 'staff_email' in str(e):
                        error = {
                            'error':'email-error'
                        }
                    else:
                        error = {
                            'error':'else'
                        }
            else:
                error = {
                    'error':'password-mismatched'
                }
        else:
            error = {
                'error':'empty-fields'
            }
        return render(request,'Patient/signup.html',context=error)

    return render(request,'Patient/signup.html')

def staff_login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        if all([email,password]):
            check_email = models.Staff.objects.filter(staff_email=email).exists()
            if check_email:
                staff = models.Staff.objects.get(staff_email=email)
                check_pass = check_password(password,staff.staff_password)
                if check_pass:
                    request.session['staff_id'] = staff.staff_id
                    request.session['staff_name'] = staff.staff_name
                    request.session['staff_designation'] = staff.staff_designation
                    return redirect('Home_page')
                else:
                    error = {
                        'error':'not-matched'
                    }
            else:
                error = {
                    'error':'not-matched'
                }
        else:
            error = {
                'error':'empty-fields'
            }
        return render(request,'Patient/login.html',context=error)


    return render(request,'Patient/login.html')

def logout(request):
    request.session.pop('staff_id')
    request.session.pop('staff_name')
    request.session.pop('staff_designation')
    return redirect('Patient:login')