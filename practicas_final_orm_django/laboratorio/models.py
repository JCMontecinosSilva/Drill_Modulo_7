from django.db import models


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100) 
    
    ciudad = models.CharField(max_length=100, default=" ") 
    pais = models.CharField(max_length=100, default=" ")  
    
    def __str__(self):
        return self.nombre 
    
    class Meta:
        ordering = ['nombre']  


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)    
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)    
    especialidad = models.CharField(max_length=100, default=" ")  

    def __str__(self):
        return f"{self.nombre} - {self.laboratorio.nombre}"  

    class Meta:
        ordering = ['nombre']  



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
    f_fabricacion = models.DateField()  
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)  
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)  
    
    class Meta:
        ordering = ['nombre']  
    
    def get_year_fabricacion(self):
        return self.f_fabricacion.year  
    
    

class BoardsModel(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    modificado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo