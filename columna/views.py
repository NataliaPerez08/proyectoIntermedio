from django.shortcuts import render
from .models import Columna
from django.template.loader import render_to_string
from notas.models import Nota
from django.http import HttpResponse

# Create your views here.
def createColumn(request, pk):
    # Obtenemos la columna que vamos a mostrar
    columna = Columna.objects.get(pk=pk)
    # Obtenemos las notas que pertenecen a esa columna
    notas = Nota.objects.filter(columna=columna)
    columna = render_to_string('columna.html', {"columna": columna, "notas": notas}, request=request)
    return columna
    #return render(request, 'columna.html', 
     #             {
      #                "columna": columna,
       #               "notas" : notas
        #              })