# Generated by Django 5.1.3 on 2024-11-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('meta_description', models.CharField(max_length=160)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]