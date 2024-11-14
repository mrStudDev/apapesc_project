from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from ckeditor_uploader.fields import RichTextUploadingField

# Choices para reutilização
SEXO_CHOICES = [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Não declarado', 'Não declarado'),
]

UF_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'),
    ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'),
    ('TO', 'Tocantins'), ('UF', 'UF'),
]


EMISSOR_RG_CHOICES = [
    ('SSP/AC', 'SSP/AC'),
    ('SSP/AL', 'SSP/AL'),
    ('SSP/AP', 'SSP/AP'),
    ('SSP/AM', 'SSP/AM'),
    ('SSP/BA', 'SSP/BA'),
    ('SSP/CE', 'SSP/CE'),
    ('SSP/DF', 'SSP/DF'),
    ('SSP/ES', 'SSP/ES'),
    ('SSP/GO', 'SSP/GO'),
    ('SSP/MA', 'SSP/MA'),
    ('SSP/MG', 'SSP/MG'),
    ('SSP/MS', 'SSP/MS'),
    ('SSP/MT', 'SSP/MT'),
    ('SSP/PA', 'SSP/PA'),
    ('SSP/PB', 'SSP/PB'),
    ('SSP/PE', 'SSP/PE'),
    ('SSP/PI', 'SSP/PI'),
    ('SSP/RJ', 'SSP/RJ'),
    ('SSP/RN', 'SSP/RN'),
    ('SSP/RS', 'SSP/RS'),
    ('SSP/RO', 'SSP/RO'),
    ('SSP/RR', 'SSP/RR'),
    ('SSP/SC', 'SSP/SC'),
    ('SSP/SP', 'SSP/SP'),
    ('SSP/SE', 'SSP/SE'),
    ('SSP/TO', 'SSP/TO'),
    ('UF', 'UF'),
]

STATUS_CHOICES = [
    ('Ativo(a)', 'Ativo(a)'),
    ('Aposentado(a)', 'Aposentado(a)'),
]

class MunicipiosCircusnscricaoModel(models.Model):
    municipio = models.CharField(max_length=120)

    def __str__(self):
        return self.municipio


class ReparticaoModel(models.Model):
    nome_reparticao = models.CharField(max_length=120)
    municipio_sede = models.ForeignKey(
        MunicipiosCircusnscricaoModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='sedes'
    )  # Relaciona com o município sede

    delegado_responsavel = models.CharField(max_length=120)
    email_delegado = models.EmailField(unique=True, blank=True, null=True)
    celular_delegado = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                r'^\(\d{2}\)\d{5}-\d{4}$',  # Garante que o número seja no formato (XX)XXXXX-XXXX
                'Número inválido. O telefone deve conter 10 ou 11 dígitos, ex: (48)99999-9999.'
            )
        ]
    )
    municipios_circunscricao = models.ManyToManyField(MunicipiosCircusnscricaoModel, related_name='reparticoes', blank=True)  # Relação muitos-para-muitos com municípios

    def __str__(self):
        return self.nome_reparticao


# Create your models here.
class AssociadoModel(models.Model):
    # Informações Pessoais
    nome_completo = models.CharField(
        max_length=100, verbose_name="Nome Completo", help_text="Informe o nome completo do associado"
    )
    cpf = models.CharField(
        max_length=14, unique=True,
        validators=[RegexValidator(r'^\d{11}$', 'CPF deve conter exatamente 11 dígitos.')],
        verbose_name = "CPF"
    )
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

    foto = models.ImageField(upload_to='fotos_associados/', blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    # Documento RG
    rg_numero = models.CharField(max_length=20, unique=True, verbose_name="Número do RG", blank=True, null=True)
    rg_orgao = models.CharField(
        max_length=10,
        choices=EMISSOR_RG_CHOICES,
        default='UF',  # Um valor padrão, se necessário,
        verbose_name="RG-Orgão Emissor"
    )
    rg_data_emissao = models.DateField(blank=True, null=True, verbose_name="Data Emissão do RG")
    naturalidade = models.CharField(max_length=100, blank=True, null=True)
    sexo_biologico = models.CharField(max_length=15, choices=SEXO_CHOICES, default="Não declarado",
                                      verbose_name="Sexo Biológico")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe", blank=True, null=True)
    nome_pai = models.CharField(max_length=100, verbose_name="Nome do Pai", blank=True, null=True)

    # Documentos/Números Cidadão INSS/NIT/PIS/TITULO
    nit = models.CharField(max_length=25, blank=True, null=True, verbose_name="Número do NIT", unique=True)
    pis = models.CharField(max_length=25, blank=True, null=True, verbose_name="Número do PIS")
    titulo_eleitor = models.CharField(max_length=20, blank=True, null=True, verbose_name="Número do Título de Eleitor")

   # Documentação Profissional
    rgp = models.CharField(max_length=25, blank=True, null=True, verbose_name="Número do RGP", unique=True)
    rgp_data_emissao = models.DateField(blank=True, null=True, verbose_name="Data Emissão do RGP")
    primeiro_registro = models.DateField(blank=True, null=True, verbose_name="Data Primeiro Registro (RGP)")
    rgp_mpa = models.CharField(blank=True, null=True, max_length=12, verbose_name="Mapa do RGP")

    # Documentação de Trabalho
    ctps = models.CharField(max_length=25, blank=True, null=True, unique=True,
                            verbose_name="Número Carteira Trabalho (CTPS)")
    ctps_serie = models.CharField(max_length=25, blank=True, null=True, verbose_name="CTPS - Série")
    ctps_data_emissao = models.DateField(blank=True, null=True, verbose_name="Data Emissão da CTPS")
    ctps_uf = models.CharField(blank=True, null=True, max_length=2, choices=UF_CHOICES, default="UF",
                               verbose_name="CTPS UF")
    # Documentação de Hanbilitação
    cnh = models.CharField(max_length=25, blank=True, null=True, unique=True, verbose_name="Núm. Registro da CNH")
    cnh_data_emissao = models.DateField(blank=True, null=True, verbose_name="Data Emissão da CNH")

    # Endereço residencial
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
    uf = models.CharField(max_length=2, choices=UF_CHOICES, default="SC", blank=True, null=True, verbose_name="UF")

    # Acesso ao Governo
    user_gov = models.CharField(max_length=25, blank=True, null=True)
    senha_gov = models.CharField(
        max_length=128, blank=True, null=True,
        help_text="Senha criptografada para segurança."
    )
    municipio_circunscricao = models.ForeignKey(MunicipiosCircusnscricaoModel, on_delete=models.SET_NULL, null=True,
                                                blank=True, related_name='associados', verbose_name="Município de Circunscrição")
    reparticao = models.ForeignKey(ReparticaoModel, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='associados', verbose_name="Nome da Repartição")
    data_cadastro = models.DateField(null=True, blank=True, verbose_name="Data da Filiação")
    status = models.CharField(max_length=40, blank=True, null=True, choices=STATUS_CHOICES,
                              verbose_name="Status",
                              default="Ativo(a)")
    data_atualizacao = models.DateTimeField(auto_now=True)
    # Anotações
    content = RichTextUploadingField(blank=True, null=True, verbose_name="Anotações")


    def save(self, *args, **kwargs):
        if not self.data_cadastro:
            self.data_cadastro = timezone.now()  # Garantir que a data de cadastro seja definida na primeira vez
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.nome_completo} - CPF: {self.cpf} - CELULAR: {self.celular} - {self.data_nascimento}"

    class Meta:
        verbose_name = "Associado"
        verbose_name_plural = "Associados"
        ordering = ['nome_completo']

