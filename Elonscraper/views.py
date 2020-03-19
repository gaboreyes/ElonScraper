from django.http import HttpResponse

#funciones que se disparan al visitar una url

def spacex(request):
  return HttpResponse("Spacex")

def tesla(request):
  return HttpResponse("Tesla")

def twitter(request):
  return HttpResponse("Twitter")



