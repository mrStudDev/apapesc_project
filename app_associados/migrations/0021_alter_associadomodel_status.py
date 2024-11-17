# Generated by Django 5.1.3 on 2024-11-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0020_associadomodel_profissao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associadomodel',
            name='status',
            field=models.CharField(blank=True, choices=[('Associado Lista Ativo(a)', 'Associado Lista Ativo(a)'), ('Associado Lista Aposentado(a)', 'Associado  Lista Aposentado(a)'), ('Desassociado(a)', 'Desassociado(a)'), ('Candidato(a)', 'Candidato(a)'), ('Cliente Especial', 'Cliente Especial')], default='Associado Lista Ativo(a)', max_length=40, null=True, verbose_name='Status'),
        ),
    ]