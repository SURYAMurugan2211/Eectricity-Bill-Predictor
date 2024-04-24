'''from django.db import models

# Create your models here.
class django_back(models.Model):
    Fan=models.FloatField()
    Refrigerator=models.FloatField()
    Television=models.FloatField()
    MonthlyHours=models.FloatField()'''
from django.db import models

class Dataset(models.Model):
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Prediction(models.Model):
    result = models.FloatField()
