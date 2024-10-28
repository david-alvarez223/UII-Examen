from django.db import models

# Create your models here.
class Productos(models.Model):

    id=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name=("Producto")
        verbose_name_plural=("Productos")