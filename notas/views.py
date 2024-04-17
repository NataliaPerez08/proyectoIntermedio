from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages



from .models import Nota
from .forms import CrearNotaForm, EditarNotaForm
import datetime


def index(request):
    return render(request,'notas/index.html')

def home(request):
    """
    Crea notas usando crispy forms.
    """
    notas = Nota.objects.all()
    form = CrearNotaForm()
    
    if request.method == "POST":
        form = CrearNotaForm(request.POST)
        
        if form.is_valid():
            nota = form.save(commit=False)
            nota.autor = request.user
            nota.save()
            
            return redirect('notas:home')
            
    contexto = {
        'notas':notas,
        'form':form
    }
    return  render(request,'notas/home.html', contexto) 

def editar(request, id):
    """
    Edita notas usando crispy forms.
    """
    nota = Nota.objects.get(id)
    form = EditarNotaForm(instance=nota)
    
    if request.method == 'POST':
        form = EditarNotaForm(request.POST)
        
        if form.is_valid():
            nota.titulo = form.cleaned_data["titulo"]
            nota.contenido = form.cleaned_data["contenido"]
            
            nota.save()
            return redirect('notas:home')
    
    contexto = {
        'nota':nota,
        'form':form
    }
    
    return render(request, 'notas/update.html', contexto)

def eliminar(request, id):
    """
    Dado un id, elimina la nota.
    """
    nota = Nota.objects.get(id)
    nota.delete()
    
    return redirect('notas:home')

def registrar(request):
    """
    Registra un nuevo usuario y redirecciona al index.
    """
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "La cuenta ha sido registrada")
            
            return redirect('notas:login')
            
    contexto = {
        'form':form
    }
    return render(request, 'notas/signup.html', contexto)