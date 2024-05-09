from django.shortcuts import render,HttpResponse

def home(request):
    name = 'Sukhdeep Singh'
    age = 24
    city = 'Nawanshahr'

    data = {
        'name':name,
        'my_age':age,
        'city':city,
        'fev_color':'Red'
    }
    return render(request,'home.html',context=data)
