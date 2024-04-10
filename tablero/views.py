from django.shortcuts import render
from django.http import HttpResponse
from columna.views import createColumn

# Create your views here.
def index(request):
    columna = createColumn(request, 1)
    return render(request, 'tablero.html', {'columna':columna})
