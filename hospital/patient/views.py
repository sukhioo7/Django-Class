from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'Sukhdeep'
    age = 34
    data = {
        'username':name,
        'age':age
    }
    return render(request,'patient/home.html',context=data)

def contact(request):
    return render(request,'patient/contact.html')