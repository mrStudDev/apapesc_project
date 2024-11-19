from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator

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
    ('TO', 'Tocantins'),
    ('Não declarado', 'Não declarado'),
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
    ('Não declarado', 'Não declarado'),
]

STATUS_CHOICES = [
    ('Associado Lista Ativo(a)', 'Associado Lista Ativo(a)'),
    ('Associado Lista Aposentado(a)', 'Associado  Lista Aposentado(a)'),
    ('Desassociado(a)', 'Desassociado(a)'),
    ('Candidato(a)', 'Candidato(a)'),
    ('Cliente Especial', 'Cliente Especial'),
]
ESPECIES_MARITIMAS = [
    ('Pampo', 'Pampo'),
    ('Abrótea', 'Abrótea'),
    ('Tainha', 'Tainha'),
    ('Anchova', 'Anchova'),
    ('Robalo', 'Robalo'),
    ('Sardinha', 'Sardinha'),
    ('Atum', 'Atum'),
    ('Corvina', 'Corvina'),
    ('Pescada-olhuda', 'Pescada-olhuda'),
    ('Linguado', 'Linguado'),
    ('Garoupa', 'Garoupa'),
    ('Bagre', 'Bagre'),
    ('Baiacu', 'Baiacu'),
    ('Cavala', 'Cavala'),
    ('Xerelete', 'Xerelete'),
    ('Cação', 'Cação'),
    ('Marisco', 'Marisco'),
    ('Não declarado', 'Não declarado'),
]
ESTADO_CIVIL_CHOICES = [
    ('solteiro', 'solteiro'),
    ('solteira', 'solteira'),
    ('casado', 'casado'),
    ('casada', 'casada'),
    ('divorciado', 'divorciado'),
    ('divorciada', 'divorciada'),
    ('viúvo', 'viúvo'),
    ('viúva', 'viúva'),
    ('união estável', 'união estável'),  # Mantido original para consistência
    ('separado judicialmente', 'separado judicialmente'),
    ('separada judicialmente', 'separada judicialmente'),
    ('Não declarado', 'Não declarado'),

]
PROFISSAO_CHOICES = [
    ('Pescador Profissional', 'Pescador Profissional'),
    ('Pescadora Profissional', 'Pescadora Profissional'),
    ('Aposentado', 'Aposentado'),
    ('Aposentada', 'Aposentada'),
    ('Profissional Autônomo', 'Profissional Autônomo'),
    ('Empresário', 'Empresário'),
    ('Empresária', 'Empresária'),
    ('Comerciante', 'Comerciante'),
    ('Professor', 'Professor'),
    ('Professora', 'Professora'),
    ('Trabalhador Doméstico', 'Trabalhador Doméstico'),
    ('Gari', 'Gari'),
    ('Servidor Público', 'Servidor Público'),
    ('Micro Empreendedor Individual', 'Micro Empreendedor Individual'),
    ('Não declarado', 'Não declarado'),
]

ETNIA_CHOICES = [
    ('Branco', 'Branco'),
    ('Pardo', 'Pardo'),
    ('Preto', 'Preto'),
    ('Amarelo', 'Amarelo'),
    ('Indígena', 'Indígena'),
    ('Outro', 'Outro'),
    ('Não declarado', 'Não declarado'),
]
ESCOLARIDADE_CHOICES = [
    ('Analfabeto', 'Analfabeto'),
    ('Primário 1/4 série', 'Primário 1/4 série'),
    ('Fundamental', 'Fundamental'),
    ('Ensino Médio', 'Ensino Médio'),
    ('Ensino Superior', 'Ensino Superior'),
    ('Não declarado', 'Não declarado'),
]
RECOLHE_INSS_CHOICES = [
    ('Sim', 'Sim'),
    ('Não', 'Não'),
    ('Não declarado', 'Não declarado'),
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

    # Endereço Repartição
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
    celular_correspondencia = models.CharField(
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
    sexo_biologico = models.CharField(max_length=15, choices=SEXO_CHOICES, default="Não declarado",
                                      verbose_name="Sexo Biológico")
    etnia = models.CharField(max_length=15, choices=ETNIA_CHOICES, default="Não declarado",
                                      verbose_name="Etnia")
    escolaridade = models.CharField(max_length=20, choices=ESCOLARIDADE_CHOICES, default="Não declarado",
                                      verbose_name="Escolaridade")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe", blank=True, null=True)
    nome_pai = models.CharField(max_length=100, verbose_name="Nome do Pai", blank=True, null=True)
    estado_civil = models.CharField(
        max_length=50, choices=ESTADO_CIVIL_CHOICES, blank=True, null=True, verbose_name="Estado Civil",
        default="Não declarado"
    )
    profissao = models.CharField(max_length=50, choices=PROFISSAO_CHOICES, blank=True, null=True, default="Não declarado")
    recolhe_inss = models.CharField(max_length=50, choices=RECOLHE_INSS_CHOICES, blank=True, null=True, default="Não declarado")
    # Documento RG
    rg_numero = models.CharField(max_length=20, unique=True, verbose_name="Número do RG", blank=True, null=True)
    rg_orgao = models.CharField(
        max_length=50,
        choices=EMISSOR_RG_CHOICES,
        default='Não declarado',  # Um valor padrão, se necessário,
        verbose_name="RG-Orgão Emissor"
    )
    rg_data_emissao = models.DateField(blank=True, null=True, verbose_name="Data Emissão do RG")
    naturalidade = models.CharField(max_length=100, blank=True, null=True)

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
    ctps_uf = models.CharField(blank=True, null=True, max_length=50, choices=UF_CHOICES, default="Não declarado",
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
    uf = models.CharField(max_length=50, choices=UF_CHOICES, default="Não declarado", blank=True, null=True, verbose_name="Estado")

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
                              default="Associado Lista Ativo(a)")
    especie1 = models.CharField(
        max_length=50, choices=ESPECIES_MARITIMAS, blank=True, null=True, verbose_name="Espécie 1",
        default="Não declarado"
    )
    quantidade1 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        verbose_name="Quantidade 1 (Kg)"
    )

    especie2 = models.CharField(
        max_length=50, choices=ESPECIES_MARITIMAS, blank=True, null=True, verbose_name="Espécie 2",
        default="Não declarado"
    )
    quantidade2 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        verbose_name="Quantidade 2 (Kg)"
    )

    especie3 = models.CharField(
        max_length=50, choices=ESPECIES_MARITIMAS, blank=True, null=True, verbose_name="Espécie 3",
        default="Não declarado"
    )
    quantidade3 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        verbose_name="Quantidade 3 (Kg)"
    )

    especie4 = models.CharField(
        max_length=50, choices=ESPECIES_MARITIMAS, blank=True, null=True, verbose_name="Espécie 4",
        default="Não declarado"
    )
    quantidade4 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        verbose_name="Quantidade 4 (Kg)"
    )
    especie5 = models.CharField(
        max_length=50, choices=ESPECIES_MARITIMAS, blank=True, null=True, verbose_name="Espécie 5",
        default="Não declarado"
    )
    quantidade5 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        verbose_name="Quantidade 5 (Kg)"
    )
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

