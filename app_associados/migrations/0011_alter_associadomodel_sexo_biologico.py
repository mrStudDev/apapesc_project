# Generated by Django 5.1.3 on 2024-11-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0010_alter_associadomodel_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associadomodel',
            name='sexo_biologico',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='', max_length=10, null=True, verbose_name='Sexo Biológico'),
        ),
    ]
