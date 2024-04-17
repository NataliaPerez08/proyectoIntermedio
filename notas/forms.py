from django import forms 
from .models import Nota
from django.contrib.auth.models import User

class CrearNotaForm(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ["titulo", "contenido", "color"]
        
class EditarNotaForm(forms.ModelForm):
    
    class Meta:
        model = Nota
        fields = ["titulo", "contenido", "color"]