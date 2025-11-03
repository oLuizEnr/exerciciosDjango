from django.shortcuts import render
from .models import Especialidade, Medico
from .forms import MedicoForm

# Create your views here.
def cadastrar_especialidades(request):
    return render(request, "medico/cadastro_especialidade.html", )

def listar_especialidades(request):
    especialidades = Especialidade.objects.all()
    return render(request, "medico/lista_especialidade.html", {"especialidades": especialidades})

def cadastrar_medicos(request):
    form = MedicoForm()
    return render(request, "medico/cadastro_medico.html", {"form": form})

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, "medico/lista_medico.html", {"medicos": medicos})

# Luiz Enrique