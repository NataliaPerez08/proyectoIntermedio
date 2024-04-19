from django.template.loader import render_to_string
from notas.models import Nota
from .models import Columna
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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

        if(nota.autor != request.user.username):
            return HttpResponse("No puedes editar una nota que no es tuya" , status=403)
        
        # Update the object with the new values from the form
        nota.titulo = request.POST.get('titulo')
        nota.contenido = request.POST.get('contenido')
        nota.color = request.POST.get('color')
        nota.autor = request.POST.get('autor')
        nota.columna_id = request.POST.get('columna')
        
        # Save the updated object
        nota.save()
    return HttpResponseRedirect(reverse("tablero:index"))