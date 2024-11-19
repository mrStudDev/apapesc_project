from django.contrib import admin
from .models import Home
from .models import ApapescModel

@admin.register(ApapescModel)
class ApapescAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'razao_social', 'cnpj', 'email', 'celular', 'presidente')
    search_fields = ('nome_fantasia', 'razao_social', 'cnpj', 'email', 'presidente')
    list_filter = ('uf',)

admin.site.register(Home)
# Register your models here.
