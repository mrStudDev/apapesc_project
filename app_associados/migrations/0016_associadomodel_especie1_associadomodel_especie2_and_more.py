# Generated by Django 5.1.3 on 2024-11-16 17:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associados', '0015_alter_associadomodel_ctps_uf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='associadomodel',
            name='especie1',
            field=models.CharField(choices=[('Pampo', 'Pampo'), ('Abrótea', 'Abrótea'), ('Tainha', 'Tainha'), ('Anchova', 'Anchova'), ('Robalo', 'Robalo'), ('Sardinha', 'Sardinha'), ('Atum', 'Atum'), ('Corvina', 'Corvina'), ('Pescada-olhuda', 'Pescada-olhuda'), ('Linguado', 'Linguado'), ('Garoupa', 'Garoupa'), ('Bagre', 'Bagre'), ('Baiacu', 'Baiacu'), ('Cavala', 'Cavala'), ('Xerelete', 'Xerelete'), ('Cação', 'Cação'), ('Marisco', 'Marisco')], default='Não Declarado', max_length=20, verbose_name='Espécie 1'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='especie2',
            field=models.CharField(blank=True, choices=[('Pampo', 'Pampo'), ('Abrótea', 'Abrótea'), ('Tainha', 'Tainha'), ('Anchova', 'Anchova'), ('Robalo', 'Robalo'), ('Sardinha', 'Sardinha'), ('Atum', 'Atum'), ('Corvina', 'Corvina'), ('Pescada-olhuda', 'Pescada-olhuda'), ('Linguado', 'Linguado'), ('Garoupa', 'Garoupa'), ('Bagre', 'Bagre'), ('Baiacu', 'Baiacu'), ('Cavala', 'Cavala'), ('Xerelete', 'Xerelete'), ('Cação', 'Cação'), ('Marisco', 'Marisco')], max_length=20, null=True, verbose_name='Espécie 2'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='especie3',
            field=models.CharField(blank=True, choices=[('Pampo', 'Pampo'), ('Abrótea', 'Abrótea'), ('Tainha', 'Tainha'), ('Anchova', 'Anchova'), ('Robalo', 'Robalo'), ('Sardinha', 'Sardinha'), ('Atum', 'Atum'), ('Corvina', 'Corvina'), ('Pescada-olhuda', 'Pescada-olhuda'), ('Linguado', 'Linguado'), ('Garoupa', 'Garoupa'), ('Bagre', 'Bagre'), ('Baiacu', 'Baiacu'), ('Cavala', 'Cavala'), ('Xerelete', 'Xerelete'), ('Cação', 'Cação'), ('Marisco', 'Marisco')], max_length=20, null=True, verbose_name='Espécie 3'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='especie4',
            field=models.CharField(blank=True, choices=[('Pampo', 'Pampo'), ('Abrótea', 'Abrótea'), ('Tainha', 'Tainha'), ('Anchova', 'Anchova'), ('Robalo', 'Robalo'), ('Sardinha', 'Sardinha'), ('Atum', 'Atum'), ('Corvina', 'Corvina'), ('Pescada-olhuda', 'Pescada-olhuda'), ('Linguado', 'Linguado'), ('Garoupa', 'Garoupa'), ('Bagre', 'Bagre'), ('Baiacu', 'Baiacu'), ('Cavala', 'Cavala'), ('Xerelete', 'Xerelete'), ('Cação', 'Cação'), ('Marisco', 'Marisco')], max_length=20, null=True, verbose_name='Espécie 4'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='especie5',
            field=models.CharField(blank=True, choices=[('Pampo', 'Pampo'), ('Abrótea', 'Abrótea'), ('Tainha', 'Tainha'), ('Anchova', 'Anchova'), ('Robalo', 'Robalo'), ('Sardinha', 'Sardinha'), ('Atum', 'Atum'), ('Corvina', 'Corvina'), ('Pescada-olhuda', 'Pescada-olhuda'), ('Linguado', 'Linguado'), ('Garoupa', 'Garoupa'), ('Bagre', 'Bagre'), ('Baiacu', 'Baiacu'), ('Cavala', 'Cavala'), ('Xerelete', 'Xerelete'), ('Cação', 'Cação'), ('Marisco', 'Marisco')], max_length=20, null=True, verbose_name='Espécie 5'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='quantidade1',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade 1 (Kg)'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='quantidade2',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade 2 (Kg)'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='quantidade3',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade 3 (Kg)'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='quantidade4',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade 4 (Kg)'),
        ),
        migrations.AddField(
            model_name='associadomodel',
            name='quantidade5',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade 5 (Kg)'),
        ),
    ]
