from django.urls import path
from . import views

app_name = "tablero"
urlpatterns = [
    path("", views.index, name = "index")
]