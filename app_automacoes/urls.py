from django.urls import path
from . import views

app_name = 'app_automacoes'

urlpatterns = [
    path('declaracao/filiado/<int:associado_id>/', views.gerar_declaracao_filiado,
         name='gerar_declaracao_filiado'),

    path('declaracao/atividade/<int:associado_id>/', views.gerar_declaracao_atividade_pesqueira,
         name='gerar_declaracao_atividade_pesqueira'),

    path('declaracao/residencia/<int:associado_id>/', views.gerar_declaracao_residencia,
         name='gerar_declaracao_residencia'),

    path('declaracao/hipossuficiencia/<int:associado_id>/', views.gerar_declaracao_hipo,
         name='gerar_declaracao_hipo'),

    path('procuracao/juridica/<int:associado_id>/', views.gerar_procuracao_juridica,
         name='gerar_procuracao_juridica'),

    path('certificado/<int:associado_id>/', views.gerar_certificado,
         name='gerar_certificado'),

    path('pagina-acoes/', views.pagina_acoes, name='pagina_acoes'),
    path('pagina-acoes/<int:associado_id>/', views.pagina_acoes, name='pagina_acoes'),

]