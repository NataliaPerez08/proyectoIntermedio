from django.urls import path
from . import views

urlpatterns = [
    path('update_nota/<int:nota_id>/', views.update_nota, name='update_nota'),
    path("", views.crear_nota, name="crear"),
]