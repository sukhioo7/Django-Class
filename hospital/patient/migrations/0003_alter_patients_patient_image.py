# Generated by Django 5.0.1 on 2024-02-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0002_patients_patient_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patients",
            name="patient_image",
            field=models.ImageField(null=True, upload_to="patients/"),
        ),
    ]
