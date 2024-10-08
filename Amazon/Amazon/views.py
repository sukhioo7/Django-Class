from django.shortcuts import HttpResponse,render

def home(request):
    return render(request,'home.html')

def about(request):
    who = 'Dr. Smith'
    age = 24
    profession = 'Doctor'

    data = {
        'person_name':who,
        'age':age,
        'profession':profession
    }
    return render(request,'about.html',context=data)

def contact(request):
    return render(request,'contact.html')