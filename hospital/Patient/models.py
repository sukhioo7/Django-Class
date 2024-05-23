from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True,unique=True)
    patient_name = models.CharField(max_length=300)
    patient_age = models.SmallIntegerField()
    patient_phone = models.CharField(max_length=10,unique=True)
    patient_email = models.EmailField(max_length=300,unique=True)
    patient_gender = models.CharField(max_length=20)
    patient_city = models.CharField(max_length=200)
    patient_symptoms = models.CharField(max_length=1000)
    patient_image = models.ImageField(upload_to='patient_image/',null=True)
    registered_time = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'Patient ID : {self.patient_id}, Name : {self.patient_name}'