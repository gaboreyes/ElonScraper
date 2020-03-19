from django.shortcuts import render

# Create your views here.

#funciones que se disparan al visitar una url

def tesla(request):
  return render(request, "tesla/tesla.html")