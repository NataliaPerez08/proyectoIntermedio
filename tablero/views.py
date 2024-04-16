from django.shortcuts import render
from django.http import HttpResponse
from columna.views import createColumn
from columna.models import Columna

# Create your views here.
def index(request):
    # Creamos una columna por cada categoria
    columnas = Columna.objects.all()
    # Obtenemos la pk de las columnas
    columna_keys = [columna.pk for columna in columnas]
    # Generamos cada columna con sus respectivas notas
    columnas_html = [createColumn(request, pk) for pk in columna_keys]
    return render(request, 'tablero.html', {'columnas':columnas_html})
