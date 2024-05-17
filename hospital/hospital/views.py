from django.shortcuts import render,HttpResponse

def home(request):
    name = 'Sukhdeep'

    data = {
        'my_name':name,
        'age':24,
        'subject':'Django'
    }
    return render(request,'home.html',context=data)

def contact(request):
    return render(request,'contact.html')