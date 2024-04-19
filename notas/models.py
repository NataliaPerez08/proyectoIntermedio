from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Nota(models.Model):
    
    # class Colores(models.Choices):
    #     AZUL = '#A5C8CA'
    #     AMARILLO = '#FFEBC5'
    #     MORADO = '#C5B2E4'
    #     ROSA = '#FFC7AF'
    #     VERDE = '#A9DDFF'
        
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    color = models.CharField(max_length=200)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo

