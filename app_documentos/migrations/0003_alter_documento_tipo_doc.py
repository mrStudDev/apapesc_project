# Generated by Django 5.1.3 on 2024-11-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_documentos', '0002_documento_tipo_doc_alter_documento_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='tipo_doc',
            field=models.CharField(choices=[('', ''), ('RG', 'RG'), ('CPF', 'CPF'), ('Foto 3x4', 'Foto 3x4'), ('Carteira de Trabalho CTPS', 'Carteira de Trabalho CTPS'), ('Habilitação CHN', 'Habilitação CHN'), ('Registro de Pescador RGP', 'Registro de Pescador RGP'), ('Protocolo pedido RGP', 'Protocolo pedido RGP'), ('Protocolo pedido Licença Embarcação', 'Protocolo pedido Licença Embarcação'), ('INSS Extrato de Contribuições', 'INSS Extrato de Contribuições'), ('CNIS Cadastro Nac. de Infos Sociais', 'CNIS Cadastro Nac. de Infos Sociais'), ('Carta de Concessão aposentados/pensionistas', 'Carta de Concessão aposentados/pensionistas'), ('Histórico de Créditode Benefício', 'Histórico de Créditode Benefício'), ('Dar outro nome', 'Dar outro nome')], default='Outros', max_length=100, verbose_name='Tipo do Documento'),
        ),
    ]
