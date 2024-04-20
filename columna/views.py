import datetime
from unittest import loader
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from notas.models import Nota
from .models import Columna
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def createColumn(request, pk):
    # Obtenemos la columna que vamos a mostrar
    columna = Columna.objects.get(pk=pk)
    # Obtenemos las notas que pertenecen a esa columna
    notas = Nota.objects.filter(columna=columna)
    columna = render_to_string('columna.html', {"columna": columna, "notas": notas}, request=request)
    return columna 

def update_nota(request, nota_id):
    if request.method == 'POST':
        # Get the Nota object to update
        nota = Nota.objects.get(pk=nota_id)

        if(nota.autor != request.user):
            return HttpResponse("No puedes editar esta nota", status=403)
        
        # Update the object with the new values from the form
        nota.titulo = request.POST.get('titulo')
        nota.contenido = request.POST.get('contenido')
        nota.color = request.POST.get('color')
        nota.autor = request.POST.get('autor')
        nota.columna_id = request.POST.get('columna')
        
        # Save the updated object
        nota.save()
    return HttpResponse("Nota editada de manera exitosa", status=200)



def crear_nota(request):
   
    if request.method == "POST":
     
        fecha_actual = datetime.datetime.now() 
        
     
        titulo    = request.POST["titulo"]
        contenido = request.POST["contenido"]
        color     = request.POST["color"]
        user      = request.user 
        columna   = request.POST["columna"]
        columna   = Columna.objects.get(pk=columna)
       
        if not titulo or not contenido or not color:
            return HttpResponse("Debes completar todos los campos")

        n = Nota(titulo=titulo, contenido=contenido, color=color, autor=user, fecha_modificacion=fecha_actual, columna=columna)
        n.save()
        
        # return HttpResponse("La nota ha sido guardada", status=200)
        
        columnas = Columna.objects.all()
        
        contexto = {
            "columnas": columnas
        }
        
        return  HttpResponseRedirect(reverse("tablero:index"))
    
    # else:
    #     columnas = Columna.objects.all()
    #     template = loader.get_template("columna/columna.html")
     
    #     return HttpResponse(template.render({"columnas": columnas}, request))
