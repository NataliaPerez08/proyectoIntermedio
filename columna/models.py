from django.db import models

# Create your models here.
class Columna(models.Model):
    titulo = models.CharField(max_length=25)