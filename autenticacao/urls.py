from autenticacao import views
from django.urls import path

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
]