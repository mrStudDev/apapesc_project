from django.db import models
from django.utils import timezone
from app_associados.models import AssociadoModel

TIPO_DOC_CHOICES = [
    ('', ''),
    ('RG', 'RG'),
    ('CPF', 'CPF'),
    ('Foto 3x4', 'Foto 3x4'),
    ('Carteira de Trabalho CTPS', 'Carteira de Trabalho CTPS'),
    ('Habilitação CHN', 'Habilitação CHN'),
    ('Registro de Pescador RGP', 'Registro de Pescador RGP'),
    ('Protocolo pedido RGP', 'Protocolo pedido RGP'),
    ('Protocolo pedido Licença Embarcação', 'Protocolo pedido Licença Embarcação'),
    ('INSS Extrato de Contribuições', 'INSS Extrato de Contribuições'),
    ('CNIS Cadastro Nac. de Infos Sociais', 'CNIS Cadastro Nac. de Infos Sociais'),
    ('Carta de Concessão aposentados/pensionistas', 'Carta de Concessão aposentados/pensionistas'),
    ('Histórico de Créditode Benefício', 'Histórico de Créditode Benefício'),
    ('Nomear documento...', 'Nomear documento...'),



]


class Documento(models.Model):
    associado = models.ForeignKey(
        AssociadoModel, on_delete=models.CASCADE, related_name='documentos',
        verbose_name="Associado"
    )
    tipo_doc = models.CharField(
        max_length=100, choices=TIPO_DOC_CHOICES, default="Outros",
        verbose_name="Tipo do Documento"
    )
    nome = models.CharField(max_length=255, verbose_name="Nome do Documento", blank=True)
    arquivo = models.FileField(upload_to='documentos/', verbose_name="Arquivo")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_upload = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")

    def save(self, *args, **kwargs):
        # Recupera o nome do associado e a data formatada
        nome_associado = self.associado.nome_completo
        data_str = timezone.now().strftime('%Y-%m-%d')

        if self.tipo_doc == 'Nomear documento...':
            if self.nome:
                # Se "Dar outro nome" estiver selecionado e o usuário digitou um valor
                self.nome = f"{self.nome} - {nome_associado} - {data_str}"
            else:
                # Se o usuário não digitou um nome, pode lançar um erro ou definir um valor padrão
                self.nome = f"Documento sem nome - {nome_associado} - {data_str}"
        else:
            # Independente do que o usuário digitou em 'nome', usamos 'tipo_doc' como base
            self.nome = f"{self.tipo_doc} - {nome_associado} - {data_str}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.associado}"
