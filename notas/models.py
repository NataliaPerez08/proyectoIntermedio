from django.db import models
from columna.models import Columna

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    color = models.CharField(max_length=20)
    autor = models.CharField(max_length=100 )
    fecha_modificacion = models.DateTimeField('fecha de modificación')
    # Por ahora se eliminan en cascada, lo cambio despues
    columna = models.ForeignKey(Columna, on_delete = models.CASCADE)
    # Podriamos agregar un campo de imagen
    # imagen = models.ImageField(upload_to='notas/imagenes/')
    def __str__(self):
        return self.titulo
    def resumen(self):
        return self.contenido[:60] + '...'