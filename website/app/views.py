from django.shortcuts import render,HttpResponse

# Create your views here.
def patient(request):
    return render(request,'app/patient.html')