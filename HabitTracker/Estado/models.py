from django.db import models

# Create your models here.
class Estado(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre