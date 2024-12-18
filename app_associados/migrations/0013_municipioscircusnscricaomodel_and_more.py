# Generated by Django 5.1.3 on 2024-11-13 18:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0012_alter_associadomodel_sexo_biologico'),
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipiosCircusnscricaoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='associadomodel',
            name='localidade_apapesc',
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='municipio_circunscricao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='associados', to='app_associados.municipioscircusnscricaomodel'),
        ),
        migrations.CreateModel(
            name='ReparticaoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_reparticao', models.CharField(max_length=120)),
                ('delegado_responsavel', models.CharField(max_length=120)),
                ('email_delegado', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('celular_delegado', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\(\\d{2}\\)\\d{5}-\\d{4}$', 'Número inválido. O telefone deve conter 10 ou 11 dígitos, ex: (48)99999-9999.')])),
                ('municipio_sede', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sedes', to='app_associados.municipioscircusnscricaomodel')),
                ('municipios_circunscricao', models.ManyToManyField(blank=True, related_name='reparticoes', to='app_associados.municipioscircusnscricaomodel')),
            ],
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='reparticao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='associados', to='app_associados.reparticaomodel'),
        ),
    ]
