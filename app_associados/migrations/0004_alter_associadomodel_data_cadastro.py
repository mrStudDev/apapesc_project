# Generated by Django 5.1.3 on 2024-11-10 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0003_alter_associadomodel_rg_orgao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associadomodel',
            name='data_cadastro',
            field=models.DateField(blank=True, null=True),
        ),
    ]
