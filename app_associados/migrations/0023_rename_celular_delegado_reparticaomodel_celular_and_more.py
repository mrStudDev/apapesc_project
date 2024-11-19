# Generated by Django 5.1.3 on 2024-11-18 21:32

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
    ]