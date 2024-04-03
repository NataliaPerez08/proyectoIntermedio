from django.urls import path

from . import views
app_name = "notas"  
urlpatterns = [
    path("", views.index, name="index"),
    # ex: /notas/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /notas/crear/
    path("crear/", views.form_crear, name="crear"),
]