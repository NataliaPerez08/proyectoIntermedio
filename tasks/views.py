from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login

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
                    #print(request.POST)
                    #print("Obteniendo datos")
                    user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                    user.save()
                    # Rederigir a la pagina de las notas
                    return render(request, 'notas/index.html')
                except:
                    return HttpResponse('El usuario ya existe')
            return HttpResponse('las password no coinciden')
        
def login_user(request):
    if(request.method=='GET'):
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    if(request.method=='POST'):
        username = request.POST.get('username', '') 
        password = request.POST['password']
        if(request.POST['username']=='' or request.POST['password']==''):
            return HttpResponse('Usuario o contraseña vacios')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            template = loader.get_template("notas/index.html")
            return render(request, 'notas/index.html')
        else:
            return HttpResponse('Usuario o contraseña incorrectos')


def logout_user(request):
    logout(request)
    # Redirigir a la pagina de inicio
    return redirect('home')
        
        