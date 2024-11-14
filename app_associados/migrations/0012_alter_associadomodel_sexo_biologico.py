# Generated by Django 5.1.3 on 2024-11-13 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0011_alter_associadomodel_sexo_biologico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associadomodel',
            name='sexo_biologico',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='', max_length=10, verbose_name='Sexo Biológico'),
        ),
    ]
