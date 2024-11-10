from django.db import models


class Home(models.Model):
    nome = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.nome}"