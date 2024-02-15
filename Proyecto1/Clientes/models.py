from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pago(models.Model):
    tarjetaCredito = models.BooleanField()
    tarjetaDebito = models.BooleanField()
    transferencia = models.BooleanField()
    efectivo = models.BooleanField()
    def __str__(self):
        return f'Medio de Pago {self.id}'

class Producto(models.Model):
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=50)
    precio = models.FloatField()
    def __str__(self):
        return f"{self.cantidad} {self.producto}, {self.color}"
    

class Sucursal(models.Model):
    direccion = models.CharField(max_length=50)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
    def __str__(self):
        return f"{self.direccion} {self.numero}, {self.ciudad}"
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   
