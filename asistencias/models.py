from django.db import models

class Contacto(models.Model):
    tipo_documento = models.CharField(max_length=30)
    documento = models.CharField(max_length=15)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    fecha = models.DateField()
    asistio = models.BooleanField()

    def __str__(self):
        return self.nombre
