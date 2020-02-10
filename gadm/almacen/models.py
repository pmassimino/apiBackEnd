from django.db import models

# Create your models here.
class Familia(models.Model):
      nombre = models.CharField(max_length=100)
def __str__(self):
      return self.nombre
def __unicode__(self):
      return self.nombre

class CondIvaOp(models.Model):
      nombre = models.CharField(max_length=100)
      codigo = models.CharField(max_length=2)
def __unicode__(self):
      return self.nombre
def __str__(self):
      return self.nombre

class Articulo(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    familia= models.ForeignKey(Familia, on_delete=models.CASCADE)
    costoVenta = models.DecimalField(max_digits=18, decimal_places=4) 
    impuestoVenta =  models.DecimalField(max_digits=18, decimal_places=4) 
    alicuotaIva =  models.DecimalField(max_digits=5, decimal_places=2) 
    condIva = models.ForeignKey(CondIvaOp, on_delete=models.CASCADE)
    margenVenta = models.DecimalField(max_digits=18, decimal_places=4) 
    precioVenta = models.DecimalField(max_digits=18, decimal_places=4) 
    precioVentaFinal = models.DecimalField(max_digits=18, decimal_places=4) 

def __str__(self):
        return self.nombre