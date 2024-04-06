import datetime
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Nota


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

        # Creo una nueva nota
        n = Nota(titulo=request.POST["titulo"], contenido=request.POST["contenido"], color=request.POST["color"], autor=request.POST["autor"], fecha_modificacion=fecha_actual)
        print(n)
        # Guardo la nota
        n.save()
        # Redirijo a la lista de notas
        return HttpResponseRedirect(reverse("notas:index"))
    else:
        # Cargo el template
        template = loader.get_template("notas/create.html")
        # Renderizo el template
        return HttpResponse(template.render({}, request))

def form_editar(request, id_nota):
    try:
        nota = Nota.objects.get(pk=id_nota)
    except Nota.DoesNotExist:
        raise Http404("La nota no existe")
    if request.method == "POST":
        nota.titulo = request.POST["titulo"]
        nota.contenido = request.POST["contenido"]
        nota.color = request.POST["color"]
        nota.autor = request.POST["autor"]
        nota.fecha_modificacion = datetime.datetime.now()
        nota.save()
        return HttpResponseRedirect(reverse("notas:index"))
    else:
        return render(request, "notas/edit.html", {"nota": nota})