from django.db import models

# Create your models here.
class Especialidade(models.Model):
    nome_especialidade = models.CharField(max_length=30, null=False)
    descricao_especialidade = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nome_especialidade}: {self.descricao_especialidade}"

class Medico(models.Model):
    nome_medico = models.CharField(max_length=30, null=False)
    endereco_medico = models.CharField(max_length=60)
    telefone_medico = models.CharField(max_length=13)
    email_medico = models.CharField(max_length=60)
    ddn_medico = models.DateField(max_length=8, null=False)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    especialidade = models.ManyToManyField(Especialidade)

    def __str__(self):
        return f"Médico(a): {self.nome_medico}. Especialidades: {", ".join([e.nome_especialidade for e in self.especialidade.all()])}"
    
# Código de Luiz Enrique