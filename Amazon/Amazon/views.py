from django.shortcuts import HttpResponse,render

def home(request):
    return render(request,'home.html')

def about(request):
    who = 'Dr. Smith'
    age = 24
    profession = 'Developer'

    data = {
        'person_name':who,
        'intro':'heLLo My nAmE is sMith',
        'age':age,
        'profession':profession,
        'subject': ['Python','PHp','C++','Java','JavaScript'],
        'qualifications': {
            'graduation_year':2015,
            'university':'XYZ University',
            'major':'Computer Science'
        }
    }
    return render(request,'about.html',context=data)

def contact(request,name,age):
    data = {
        'name':name,
        'age':age,
    }
    return render(request,'contact.html',context=data)