import datetime
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Nota
from columna.models import Columna
from django.template.loader import render_to_string


def index(request):
    notas_recientes = Nota.objects.order_by("-fecha_modificacion")[:5]
    template = loader.get_template("notas/index.html")
    contexto = {
        "notas_recientes": notas_recientes,
    }
    return HttpResponse(template.render(contexto, request))

def detail(request, id_nota):
    try:
        nota = Nota.objects.get(pk=id_nota)
    except Nota.DoesNotExist:
        raise Http404("La nota no existe")
    return render(request, "notas/detail.html", {"nota": nota})

def form_crear(request):
    # Si el formulario fue enviado
    if request.method == "POST":
        # Recupero la fecha actual
        fecha_actual = datetime.datetime.now() 
        
        #  Valiadcion de los datos
        titulo = request.POST["titulo"]
        contenido = request.POST["contenido"]
        color = request.POST["color"]
        user = request.user 
        columna = request.POST["columna"]
        columna = Columna.objects.get(pk=columna)
        # Si esta vacio algun campo aviso al usuario
        if not titulo or not contenido or not color:
            return HttpResponse("Debes completar todos los campos")

        # Creo una nueva nota
        n = Nota(titulo=titulo, contenido=contenido, color=color, autor=user, fecha_modificacion=fecha_actual, columna=columna)
        # Guardo la nota
        n.save()
        # Redirijo a la lista de notas
        return HttpResponseRedirect(reverse("tablero:index"))
    else:
        columnas = Columna.objects.all()
        # Cargo el template
        template = loader.get_template("notas/create.html")
        # Renderizo el template
        return HttpResponse(template.render({"columnas": columnas}, request))

def form_editar(request, id_nota):
    try:
        nota = Nota.objects.get(pk=id_nota)
    except Nota.DoesNotExist:
        raise Http404("La nota no existe")
    if request.method == "POST":
        # Verificar si el usuario que esta editando la nota es el autor
        autor_nota = nota.autor
        usuario = request.user
        if str(autor_nota) != str(usuario):
            return HttpResponse("No puedes editar una nota que no es tuya")
        else:
            nota.titulo = request.POST["titulo"]
            nota.contenido = request.POST["contenido"]
            nota.color = request.POST["color"]
            nota.autor = request.POST["autor"]
            nota.fecha_modificacion = datetime.datetime.now()
            # Busca columna por id
            columna = Columna.objects.get(pk=request.POST["columna"])
            nota.columna = columna
            nota.save()
        return HttpResponseRedirect(reverse("tablero:index"))
    else:
        # Recupera las columnas
        columnas = Columna.objects.all()
        # Renderiza el template
        return render(request, "notas/edit.html", {"nota": nota, "columnas": columnas})