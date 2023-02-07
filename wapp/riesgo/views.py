from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "riesgo/index.html")
    
def portafolio(request):
    return HttpResponse("portafolio")
    
    