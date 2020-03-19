from django.db import models

# Create your models here.
#models.Model inherits funcionality from django 
class Spacex(models.Model):
  titulo = models.CharField(max_length=100)
  body = models.TextField()
  fecha = models.CharField(max_length=25)