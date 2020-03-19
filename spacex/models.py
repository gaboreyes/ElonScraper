from django.db import models

# Create your models here.

#models.Model inherits funcionality from django 
class SpacexItem(models.Model):
  titulo = models.CharField(max_length=100)
  body = models.TextField()
  fecha = models.CharField(max_length=25)

  #funcion que define como se vera un modelo en el admin panel
  def __str__(self):
      return self.titulo