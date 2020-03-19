from django.shortcuts import render

# Create your views here.

#funciones que se disparan al visitar una url
def spacex(request):
  return render(request, "spacex/spacex.html")