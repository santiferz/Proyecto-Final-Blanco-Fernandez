from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Futbol(models.Model):
    nombre = models.CharField(max_length=20)
    nro_equipos = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.nro_equipos}"
    
