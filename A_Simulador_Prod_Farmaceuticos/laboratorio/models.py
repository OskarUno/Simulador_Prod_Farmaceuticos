import datetime
from django.db import models
from django.core.validators import MinValueValidator

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=100, null=True)
    pais   = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, max_length=100, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f"{self.nombre} -- {self.laboratorio}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[MinValueValidator(datetime.date(2015,1,1))])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        # Validar los campos de la tabla antes de Guardar
        self.full_clean()
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f'{self.nombre} - {self.laboratorio}'
    