from django.urls import path
from . import views #Da pasta usuários import os views

urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.logar, name="login"),
    path('sair/', views.sair, name="sair"),
]