from audioop import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import Nota


def index(request):
    latest_question_list = Nota.objects.order_by("-fecha_modificacion")[:5]
    template = loader.get_template("notas/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Nota.objects.get(pk=question_id)
    except Nota.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "notas/detail.html", {"question": question})

def form_crear(request):
    # Cargo el template
    template = loader.get_template("notas/create.html")
    # Renderizo el template
    return HttpResponse(template.render({}, request))

def crear(request, Nota):
    # Creo una nueva nota
    n = Nota(titulo=request.POST["titulo"], contenido=request.POST["contenido"], color=request.POST["color"], autor=request.POST["autor"])
    # Guardo la nota
    n.save()
    # Redirijo a la lista de notas
    return HttpResponseRedirect(reverse("notas:index"))
