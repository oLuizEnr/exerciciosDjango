"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from medico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atualizarE/<int:pk>/', views.AtualizarEspecialidade.as_view()),
    path('cadastroE/', views.CadastroEspecialidade.as_view()),
    path('deletarE/<int:pk>/', views.DeletarEspecialidade.as_view()),
    path('listaE/', views.ListaEspecialidade.as_view(), name='lista_esp'),
    path('atualizarM/<int:pk>/', views.AtualizarMedico.as_view()),
    path('cadastroM/', views.CadastroMedico.as_view()),
    path('deletarM/<int:pk>/', views.DeletarMedico.as_view()),
    path('listaM/', views.ListaMedico.as_view(), name='lista_med'),
]
