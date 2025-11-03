from django.shortcuts import render
from .models import Especialidade, Medico
from .forms import MedicoForm, EspecialidadeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class AtualizarEspecialidade(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = "medico/editar_especialidade.html"
    success_url = reverse_lazy('lista_esp')
    permission_required = 'medico.change_especialidade'

class CadastroEspecialidade(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = "medico/cadastro_especialidade.html"
    success_url = reverse_lazy('lista_esp')
    permission_required = 'medico.add_medico'

class DeletarEspecialidade(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Especialidade
    template_name = "medico/excluir_especialidade.html"
    success_url = reverse_lazy('lista_esp')
    permission_required = 'medico.delete_medico'

class ListaEspecialidade(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Especialidade
    template_name = "medico/lista_especialidade.html"
    context_object_name = "especialidades"
    permission_required = 'medico.view_medico'

class AtualizarMedico(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico/editar_medico.html"
    success_url = reverse_lazy('lista_med')
    permission_required = 'medico.change_medico'

class CadastroMedico(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico/cadastro_medico.html"
    success_url = reverse_lazy('lista_med')
    permission_required = 'medico.add_medico'

class DeletarMedico(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = "medico/excluir_medico.html"
    success_url = reverse_lazy('lista_med')
    permission_required = 'medico.delete_medico'

class ListaMedico(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Medico
    template_name = "medico/lista_medico.html"
    context_object_name = "medicos"
    permission_required = 'medico.view_medico'

# Luiz Enrique