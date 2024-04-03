from django.http import Http404, HttpResponse
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
    return render(request, "polls/detail.html", {"question": question})