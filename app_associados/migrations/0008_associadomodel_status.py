# Generated by Django 5.1.3 on 2024-11-12 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0007_alter_associadomodel_data_cadastro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='associadomodel',
            name='status',
            field=models.CharField(blank=True, choices=[('Ativo', 'Ativo'), ('Aposentado', 'Aposentado')], max_length=40, null=True, verbose_name='Status'),
        ),
    ]
