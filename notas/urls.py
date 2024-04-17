from django.urls import path
from . import views
import django.contrib.auth.views as auth_views

app_name = "notas"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="notas/login.html"),
        name="login",
    ),
    path(
        "login/",
        auth_views.LogoutView.as_view(template_name="notas/index.html"),
        name="logout",
    ),
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path('signup/',views.registrar,name='signup'),
    path("editar/<int:id>", views.editar, name="editar"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar")
]
