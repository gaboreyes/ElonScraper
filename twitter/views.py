from django.shortcuts import render

# Create your views here.

#funciones que se disparan al visitar una url

def twitter(request):
  return render(request, "twitter/twitter.html")
