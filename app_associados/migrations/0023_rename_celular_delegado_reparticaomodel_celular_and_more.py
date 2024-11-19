# Generated by Django 5.1.3 on 2024-11-19 03:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0022_alter_associadomodel_quantidade1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reparticaomodel',
            old_name='celular_delegado',
            new_name='celular',
        ),
        migrations.RenameField(
            model_name='reparticaomodel',
            old_name='email_delegado',
            new_name='email',
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='celular_correspondencia',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator('^\\(\\d{2}\\)\\d{5}-\\d{4}$', 'Número inválido. O telefone deve conter 10 ou 11 dígitos, ex: (48)99999-9999.')]),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='escolaridade',
            field=models.CharField(choices=[('Analfabeto', 'Analfabeto'), ('Primário 1/4 série', 'Primário 1/4 série'), ('Fundamental', 'Fundamental'), ('Ensino Médio', 'Ensino Médio'), ('Ensino Superior', 'Ensino Superior'), ('Não declarado', 'Não declarado')], default='Não declarado', max_length=20, verbose_name='Escolaridade'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='etnia',
            field=models.CharField(choices=[('Branco', 'Branco'), ('Pardo', 'Pardo'), ('Preto', 'Preto'), ('Amarelo', 'Amarelo'), ('Indígena', 'Indígena'), ('Outro', 'Outro'), ('Não declarado', 'Não declarado')], default='Não declarado', max_length=15, verbose_name='Etnia'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='recolhe_inss',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não declarado', 'Não declarado')], default='Não declarado', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reparticaomodel',
            name='bairro',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reparticaomodel',
            name='cep',
            field=models.CharField(blank=True, default='', max_length=9, null=True, validators=[django.core.validators.RegexValidator('^\\d{8}$', 'CEP deve conter exatamente 8 dígitos.')], verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='reparticaomodel',
            name='complemento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reparticaomodel',
            name='logradouro',
            field=models.CharField(blank=True, default='', help_text='Ex: Rua, Servidão, Travessa', max_length=255, null=True, verbose_name='Logradouro'),
        ),
        migrations.AddField(
            model_name='reparticaomodel',
            name='municipio',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reparticaomodel',
            name='numero',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='reparticaomodel',
            name='uf',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('Não declarado', 'Não declarado')], default='Não declarado', max_length=50, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='associadomodel',
            name='profissao',
            field=models.CharField(blank=True, choices=[('Pescador Profissional', 'Pescador Profissional'), ('Pescadora Profissional', 'Pescadora Profissional'), ('Aposentado', 'Aposentado'), ('Aposentada', 'Aposentada'), ('Profissional Autônomo', 'Profissional Autônomo'), ('Empresário', 'Empresário'), ('Empresária', 'Empresária'), ('Comerciante', 'Comerciante'), ('Professor', 'Professor'), ('Professora', 'Professora'), ('Trabalhador Doméstico', 'Trabalhador Doméstico'), ('Gari', 'Gari'), ('Servidor Público', 'Servidor Público'), ('Micro Empreendedor Individual', 'Micro Empreendedor Individual'), ('Não declarado', 'Não declarado')], default='Não declarado', max_length=50, null=True),
        ),
    ]
