
from django.db import models
from django.core.validators import RegexValidator


UF_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'),
    ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('Não declarado', 'Não declarado'),
]



class ApapescModel(models.Model):
    nome_fantasia = models.CharField(max_length=255, verbose_name="Nome Fantasia")
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")  # Inclui máscara para validação futura

    # Dados de contato da Repartição
    celular = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                r'^\(\d{2}\)\d{5}-\d{4}$',  # Garante que o número seja no formato (XX)XXXXX-XXXX
                'Número inválido. O telefone deve conter 10 ou 11 dígitos, ex: (48)99999-9999.'
            )
        ]
    )
    email = models.EmailField(unique=True, blank=True, null=True)

    telefone = models.CharField(max_length=15, blank=True, null=True)
    # Integrantes
    fundadores = models.TextField(verbose_name="Fundadores", help_text="Lista de fundadores da associação")
    diretor = models.CharField(max_length=255, verbose_name="Diretor")
    administrador = models.CharField(max_length=255, verbose_name="Administrador")
    presidente = models.CharField(max_length=255, verbose_name="Presidente")

    # Endereço rApapesc
    logradouro = models.CharField(
        max_length=255, verbose_name="Logradouro", help_text="Ex: Rua, Servidão, Travessa",
        default="", blank=True, null=True
    )
    bairro = models.CharField(max_length=100, blank=True, null=True, default="")
    numero = models.CharField(max_length=10, default="", blank=True, null=True, verbose_name="Número")
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(
        max_length=9,  # Apenas números (sem o hífen)
        validators=[RegexValidator(r'^\d{8}$', 'CEP deve conter exatamente 8 dígitos.')],
        default="", blank=True, null=True,
        verbose_name="CEP"
    )
    municipio = models.CharField(max_length=100, default="", blank=True, null=True)
    uf = models.CharField(max_length=50, choices=UF_CHOICES, default="Não declarado", blank=True, null=True, verbose_name="Estado")

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
