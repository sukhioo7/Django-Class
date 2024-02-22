# Generated by Django 5.0.1 on 2024-02-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patients",
            fields=[
                ("patient_id", models.AutoField(primary_key=True, serialize=False)),
                ("patient_name", models.CharField(max_length=300)),
                ("patient_age", models.SmallIntegerField()),
                ("patient_gender", models.CharField(max_length=30)),
                ("patient_city", models.CharField(max_length=300)),
                ("patient_email", models.EmailField(max_length=300)),
                ("patient_phone", models.CharField(max_length=10)),
                ("patient_symptoms", models.CharField(max_length=3000)),
            ],
        ),
    ]