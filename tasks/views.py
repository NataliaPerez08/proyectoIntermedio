from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout, authenticate

# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
        if(request.method=='GET'):
            return render(request, 'signup.html', {
                'form': UserCreationForm
            })
        else:
            if(request.POST['password1']==request.POST['password2']):
                #register user
                try:
                    user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                    user.save()
                    login(request, user) 
                    return redirect('tablero')
                except:
                     return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        "error": 'el nombre de usuario ya existe'
                    })
                    
            return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        "error": 'Las contraseñas no coinciden'
                    })
        
def tablero(request):
        return render(request, 'tablero.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
          'form': AuthenticationForm
     })
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                 'form': AuthenticationForm,
                 'error': 'Usuario o contraseña incorrectas'
            })
        else:
            login(request,user)
            return redirect('tablero')
       
       
    
     
    
    
       