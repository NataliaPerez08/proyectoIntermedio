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

def detail(request, question_id):
    try:
        question = Nota.objects.get(pk=question_id)
    except Nota.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "notas/detail.html", {"question": question})

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