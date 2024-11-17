
from django.db import models

class ApapescModel(models.Model):
    nome_fantasia = models.CharField(max_length=255, verbose_name="Nome Fantasia")
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")  # Inclui máscara para validação futura
    logradouro = models.CharField(max_length=255, verbose_name="Logradouro")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Complemento")
    municipio = models.CharField(max_length=100, verbose_name="Município")
    estado = models.CharField(max_length=2, verbose_name="Estado")  # Use sigla para o estado (ex.: SC, SP, etc.)
    email = models.EmailField(max_length=100, verbose_name="Email")
    celular = models.CharField(max_length=20, verbose_name="Celular")  # Validação para formato de telefone pode ser adicionada
    fundadores = models.TextField(verbose_name="Fundadores", help_text="Lista de fundadores da associação")
    diretor = models.CharField(max_length=255, verbose_name="Diretor")
    administrador = models.CharField(max_length=255, verbose_name="Administrador")
    presidente = models.CharField(max_length=255, verbose_name="Presidente")

    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Apapesc"
        ordering = ['nome_fantasia']

    def __str__(self):
        return f"{self.nome_fantasia} ({self.razao_social})"


class Home(models.Model):
    nome = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.nome}"
