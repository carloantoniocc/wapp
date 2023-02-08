from django.shortcuts import render
from django.http import HttpResponse

from .models import Broker, Stock

def index(request):
    brokers = Broker.objects.all()
    stocks = Stock.objects.all()
    todos = Stock.objects.select_related('brokers').all()
    return render(request, "riesgo/index.html",{
        "brokers": brokers,
        "stocks": stocks,
        "todos" : todos,
    })
    
    for broker in brokers:
        print(broker.name)
    
    
    
def portafolio(request):
    return HttpResponse("portafolio")
    
    