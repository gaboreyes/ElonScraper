from django.shortcuts import render

#del directorio actual importa el modelo para poder taerte los objs de la database
from .models import SpacexItem

# Create your views here.

#funciones que se disparan al visitar una url
def spacex(request):
  #var que almacena todos los objectos de la tabla ordenados por Id
  items = SpacexItem.objects.all().order_by('id')
  return render(request, "spacex/spacex.html", {"items": items})