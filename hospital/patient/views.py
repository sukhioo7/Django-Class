from django.shortcuts import render

# Create your views here.

def home(request):
    name = "Sukhdeep"

    data = {
        'name':name,
        'age':4,
        'subject':['Python','SQL','Django','HTML','CSS','Javascript']
    }
    return render(request,'patient/home.html',context=data)

def contact(request):
    return render(request,'patient/contact.html')