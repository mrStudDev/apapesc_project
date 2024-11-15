# Generated by Django 5.1.3 on 2024-11-10 21:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociadoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(help_text='Informe o nome completo do associado', max_length=100, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator('^\\d{11}$', 'CPF deve conter exatamente 11 dígitos.')], verbose_name='CPF')),
                ('celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{10,11}$', 'Número inválido. O telefone deve conter 10 ou 11 dígitos, ex: (48)99999-9999.')])),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_associados/')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('rg_numero', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Número do RG')),
                ('rg_orgao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Órgão Emissor do RG')),
                ('rg_data_emissao', models.DateField(blank=True, null=True, verbose_name='Data Emissão do RG')),
                ('naturalidade', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo_biologico', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=10, null=True, verbose_name='Sexo Biológico')),
                ('nome_mae', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da Mãe')),
                ('nome_pai', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do Pai')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('nit', models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='Número do NIT')),
                ('pis', models.CharField(blank=True, max_length=25, null=True, verbose_name='Número do PIS')),
                ('titulo_eleitor', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número do Título de Eleitor')),
                ('rgp', models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='Número do RGP')),
                ('rgp_data_emissao', models.DateField(blank=True, null=True, verbose_name='Data Emissão do RGP')),
                ('primeiro_registro', models.DateField(blank=True, null=True, verbose_name='Data Primeiro Registro (RGP)')),
                ('rgp_mpa', models.CharField(blank=True, max_length=12, null=True, verbose_name='Mapa do RGP')),
                ('ctps', models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='Número Carteira Trabalho (CTPS)')),
                ('ctps_serie', models.CharField(blank=True, max_length=25, null=True, verbose_name='CTPS - Série')),
                ('ctps_data_emissao', models.DateField(blank=True, null=True, verbose_name='Data Emissão da CTPS')),
                ('ctps_uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='', max_length=2, null=True, verbose_name='CTPS UF')),
                ('cnh', models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='Núm. Registro da CNH')),
                ('cnh_data_emissao', models.DateField(blank=True, null=True, verbose_name='Data Emissão da CNH')),
                ('logradouro', models.CharField(blank=True, default='', help_text='Ex: Rua, Servidão, Travessa', max_length=255, null=True, verbose_name='Logradouro')),
                ('bairro', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('numero', models.CharField(blank=True, default='S/N', max_length=10, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('cep', models.CharField(blank=True, default='', max_length=9, null=True, validators=[django.core.validators.RegexValidator('^\\d{8}$', 'CEP deve conter exatamente 8 dígitos.')], verbose_name='CEP')),
                ('municipio', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SC', max_length=2, null=True, verbose_name='UF')),
                ('user_gov', models.CharField(blank=True, max_length=25, null=True)),
                ('senha_gov', models.CharField(blank=True, help_text='Senha criptografada para segurança.', max_length=128, null=True)),
                ('localidade_atuacao', models.CharField(blank=True, choices=[('Florianópolis', 'Florianópolis'), ('Balneário', 'Balneário'), ('Garopaba', 'Garopaba'), ('Laguna', 'Laguna'), ('Itapema', 'Itapema'), ('Itajai', 'Itajai'), ('Imbituba', 'Imbituba'), ('São Francisco do Sul', 'São Francisco do Sul'), ('Joinville', 'Joinville'), ('Porto Belo', 'Porto Belo'), ('Palhoça', 'Palhoça')], max_length=40, null=True, verbose_name='Localidade de Atuação')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Anotações')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Associado',
                'verbose_name_plural': 'Associados',
                'ordering': ['nome_completo'],
            },
        ),
    ]
