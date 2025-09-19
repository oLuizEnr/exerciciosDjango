from django import forms
from .models import Medico, Especialidade

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = "__all__"

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = "__all__"

# Luiz Enrique