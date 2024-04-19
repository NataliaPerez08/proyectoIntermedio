from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column
from crispy_forms.helper import FormHelper

from django import forms 
from .models import Nota

CRISPY_CLASS_CONVERTERS = {'textinput': "textinput inputtext"}

class CrearNotaForm(forms.ModelForm):
    
    COLORES = (
       ("blue", "#A5C8CA"),
       ("yellow", "#FFEBC5"),
       ("purple", "#C5B2E4"),
       ("pink", "#FFC7AF"),
       ("green", "#A9DDFF")
    )
    
    titulo = forms.CharField()
    contenido = forms.CharField()
    
    color = forms.ChoiceField(choices=COLORES, widget=forms.RadioSelect)
    
    class Meta:
        model = Nota
        fields = ["titulo", "contenido", "color"]
        
    # def __init__(self, *args, **kwargs):
        
    #     super(CrearNotaForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
        
    #     self.helper.Layout = Layout(
    #         'titulo',
    #         'contenido',   
    #     )
            
            
class EditarNotaForm(forms.ModelForm):
    
    class Meta:
        model = Nota
        fields = ["titulo", "contenido", "color"]