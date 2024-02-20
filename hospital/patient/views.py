from django.shortcuts import render

# Create your views here.

def home(request):
    full_name = request.POST['full_name'] 
    age = request.POST['age'] 
    email = request.POST['email'] 
    phone = request.POST['phone'] 
    city = request.POST['city'] 
    gender = request.POST['gender'] 
    symptoms = request.POST['symptoms'] 

    data = {
        'name':full_name,
        'age':age,
        'symptoms':symptoms
    }
    return render(request,'patient/home.html',context=data)

def contact(request):
    return render(request,'patient/contact.html')

# python manage.py runserver
