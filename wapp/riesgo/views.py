
from django.shortcuts import render
from django.http import HttpResponse


from .models import Broker, Stock

def index(request):
    # brokers = Broker.objects.all()
    # stocks = Stock.objects.all()
    stocks = Stock.objects.select_related('broker_id').all()

    print(stocks.query)
    # print("ssss", Stock.objects.select_related('broker_id').all().query)
        
    for stock in stocks:
        print(f"Nombre: {stock.name}, id: {stock.id},id: {stock.name}")
        

    return render(request, "riesgo/index.html",{
        "stocks" : stocks,
    })
    

    
    
def portafolio(request):
    return HttpResponse("portafolio")
    
    