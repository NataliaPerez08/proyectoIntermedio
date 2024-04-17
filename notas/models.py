from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    color = models.CharField(max_length=20)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo

