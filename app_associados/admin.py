from django.contrib import admin
from .models import AssociadoModel, MunicipiosCircusnscricaoModel, ReparticaoModel

@admin.register(AssociadoModel)
class AssociadoAdmin(admin.ModelAdmin):
    # Campos exibidos na listagem do admin
    list_display = ('nome_completo', 'cpf', 'email', 'celular', 'data_cadastro')
    search_fields = ('nome_completo', 'cpf', 'email')
    list_filter = ('sexo_biologico', 'uf', 'data_cadastro')

    # Sobrescreve o método save_model para preencher user_gov automaticamente
    def save_model(self, request, obj, form, change):
        if not obj.user_gov and obj.cpf:
            obj.user_gov = obj.cpf
        super().save_model(request, obj, form, change)

    # Organiza os campos em seções no formulário
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome_completo', 'foto', 'data_nascimento', 'sexo_biologico',
                       'naturalidade', 'nome_mae', 'nome_pai', 'celular', 'email')
        }),
        ('Documentação Pessoal', {
            'fields': ('cpf', 'nit', 'pis', 'rg_numero', 'rg_orgao', 'rg_data_emissao',
                       'titulo_eleitor')
        }),
        ('Documentação de Profissional', {
            'fields': ('rgp', 'rgp_data_emissao', 'primeiro_registro', 'rgp_mpa',)
        }),
        ('Documentação de Trabalho', {
            'fields': ('ctps', 'ctps_serie', 'ctps_data_emissao', 'ctps_uf')
        }),
        ('Endereço', {
            'fields': ('logradouro', 'numero', 'complemento', 'cep', 'municipio', 'uf')
        }),
        ('Anotações', {
            'fields': ('content',)
        }),
        ('Acesso ao Governo', {
            'fields': ('user_gov', 'senha_gov',)  # Adicionando 'localidade_apapesc' aqui
        }),
        # Removendo 'localidade_apapesc' da seção 'informações da Filiação'
        ('informações da Filiação', {
            'fields': ('data_cadastro',  'localidade_apapesc')  # Agora apenas 'data_cadastro' nesta seção
        }),
    )

    # Função para formatar o celular na listagem
    def formatar_celular(self, obj):
        if obj.celular:
            # Verifique se o número tem o formato correto antes de formatar
            if len(obj.celular) == 11:
                return f"({obj.celular[:2]}) {obj.celular[2:7]}-{obj.celular[7:]}"
            elif len(obj.celular) == 10:
                return f"({obj.celular[:2]}) {obj.celular[2:6]}-{obj.celular[6:]}"
        return '-'


@admin.register(MunicipiosCircusnscricaoModel)
class MunicipiosAdmin(admin.ModelAdmin):
    list_display = ('municipio',)
    search_fields = ('municipio',)


@admin.register(ReparticaoModel)
class ReparticaoAdmin(admin.ModelAdmin):
    list_display = ('nome_reparticao', 'municipio_sede', 'delegado_responsavel', 'email', 'celular')
    search_fields = ('nome_reparticao', 'delegado_responsavel', 'municipio_sede__municipio')  # Busca por nome da repartição, delegado e município sede
    filter_horizontal = ('municipios_circunscricao',)  # Widget para selecionar múltiplos municípios


    # Função para formatar o celular na listagem
    def formatar_celular(self, obj):
        if obj.celular_delegado:
            # Verifique se o número tem o formato correto antes de formatar
            if len(obj.celular_delegado) == 11:
                return f"({obj.celular_delegado[:2]}) {obj.celular_delegado[2:7]}-{obj.celular_delegado[7:]}"
            elif len(obj.celular_delegado) == 10:
                return f"({obj.celular_delegado[:2]}) {obj.celular_delegado[2:6]}-{obj.celular_delegado[6:]}"
        return '-'