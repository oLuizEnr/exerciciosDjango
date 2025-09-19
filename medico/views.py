from django.shortcuts import render
from .models import Especialidade, Medico
from .forms import MedicoForm, EspecialidadeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def cadastrar_especialidades(request):
#     return render(request, "medico/cadastro_especialidade.html", )
    
class AtualizarEspecialidade(UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = "medico/editar_especialidade.html"
    success_url = reverse_lazy('lista_esp')

class CadastroEspecialidade(CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = "medico/cadastro_especialidade.html"
    success_url = reverse_lazy('lista_esp')

class DeletarEspecialidade(DeleteView):
    model = Especialidade
    template_name = "medico/excluir_especialidade.html"
    success_url = reverse_lazy('lista_esp')

class ListaEspecialidade(ListView):
    model = Especialidade
    template_name = "medico/lista_especialidade.html"
    context_object_name = "especialidades"

# def listar_especialidades(request):
#     especialidades = Especialidade.objects.all()
#     return render(request, "medico/lista_especialidade.html", {"especialidades": especialidades})

class AtualizarMedico(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico/editar_medico.html"
    success_url = reverse_lazy('lista_med')

class CadastroMedico(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico/cadastro_medico.html"
    success_url = reverse_lazy('lista_med')

class DeletarMedico(DeleteView):
    model = Medico
    template_name = "medico/excluir_medico.html"
    success_url = reverse_lazy('lista_med')

class ListaMedico(ListView):
    model = Medico
    template_name = "medico/lista_medico.html"
    context_object_name = "medicos"

# def cadastrar_medicos(request):
#     form = MedicoForm()
#     return render(request, "medico/cadastro_medico.html", {"form": form})

# def listar_medicos(request):
#     medicos = Medico.objects.all()
#     return render(request, "medico/lista_medico.html", {"medicos": medicos})

# Luiz Enrique