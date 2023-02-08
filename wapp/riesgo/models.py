from django.db import models

# Create your models here.

class Broker(models.Model): 
    name = models.CharField(max_length=200)
    comision = models.IntegerField()
    porc_entrada = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def __str__(self):
        return  self.name

class Stock(models.Model):
    name = models.CharField(max_length=200)
    broker_id = models.ForeignKey(Broker, on_delete= models.CASCADE)

    def __str__(self):
        return  self.name

class Risk(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return  self.name

class Probability(models.Model):
    name = models.CharField(max_length=200)
    valor: models.IntegerField()

    def __str__(self):
        return  self.name

class Briefcase(models.Model):
    name = models.CharField(max_length=200)
    stock_id = models.ForeignKey(Stock, on_delete= models.CASCADE)
    broker_id = models.ForeignKey(Broker, on_delete= models.CASCADE)    
    risk_id = models.ForeignKey(Risk, on_delete= models.CASCADE)
    probability_id = models.ForeignKey(Probability, on_delete= models.CASCADE)
    cantidad = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def __str__(self):
        return  self.name

    

