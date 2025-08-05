# Create your models here.
from django.db import models

class Pedido(models.Model):
    TIPO_PEDIDO_CHOICES = [
        ('recoger', 'Recoger'),
        ('domicilio', 'Domicilio'),
    ]
    METODO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
    ]

    cliente = models.CharField(max_length=100, blank=True, null=True)
    tipo_pedido = models.CharField(max_length=10, choices=TIPO_PEDIDO_CHOICES, blank=True, null=True)
    direccion = models.TextField(blank=True)
    productos = models.TextField()
    metodo_pago = models.CharField(max_length=10, choices=METODO_PAGO_CHOICES)

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.tipo_pedido}"