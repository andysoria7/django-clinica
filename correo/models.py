from django.db import models
from django.utils import timezone
from usuarios.models import UsuarioPersonalizado

# Create your models here.

class RegistroCorreoForm(models.Model):
    asunto = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
    mensaje = models.TextField()
    destinatarios = models.ManyToManyField(UsuarioPersonalizado)
    latitud = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitud = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)
    

