from django.urls import path

from . import views
app_name = "notas"  
urlpatterns = [
    path("", views.index, name="index"),
    # ex: /notas/5/
    path("<int:id_nota>/", views.detail, name="detail"),
    # ex: /notas/crear/
    path("crear/", views.form_crear, name="crear"),
    # ex: /notas/5/editar/
    path("<int:id_nota>/editar/", views.form_editar, name="editar"),
    # ex: /notas/5/eliminar/
    path("<int:id_nota>/eliminar/", views.form_eliminar, name="eliminar"),
]