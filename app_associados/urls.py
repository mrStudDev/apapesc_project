from django.urls import path
from .views import (
    AssociadosListView,
    AssociadoDetailView,
    AssociadoCreateView,
    AssociadoUpdateView,
    AssociadoDeleteView,
    AssociadoAposentadoListView,
    AssociadoSearchView,
    MunicipiosListView,
    MunicipioCreateView,
    ReparticaoCreateView,
    MunicipioUpdateView,
    MunicipioDeleteView,
    ReparticaoUpdateView,
    ReparticaoDeleteView,
    ReparticaoListView,
    ReparticaoDetailView,
    DesassociadosListView,
    ClientesEspeciaisListView,
    CandidatosListView
)

app_name = 'app_associados'

urlpatterns = [
    path('', AssociadosListView.as_view(), name='lista_associados'),
    path('cadastrar/', AssociadoCreateView.as_view(), name='cadastrar_associado'),
    path('detalhe/<int:pk>/', AssociadoDetailView.as_view(), name='detalhe_associado'),
    path('editar/<int:pk>/', AssociadoUpdateView.as_view(), name='editar_associado'),
    path('associado/<int:pk>/delete/', AssociadoDeleteView.as_view(), name='deletar_associado'),
    path('aposentados/', AssociadoAposentadoListView.as_view(), name='lista_associados_aposentados'),
    path('buscar/', AssociadoSearchView.as_view(), name='buscar_associado'),

    path('desassociados/', DesassociadosListView.as_view(), name='lista_desassociados'),
    path('clientes_especiais/', ClientesEspeciaisListView.as_view(), name='lista_clientes_especiais'),
    path('candidatos/', CandidatosListView.as_view(), name='lista_candidatos'),

    path('lista_reparticoes/', ReparticaoListView.as_view(), name='lista_reparticoes'),
    path('reparticao/<int:pk>/', ReparticaoDetailView.as_view(), name='detail_reparticao'),
    path('criar_reparticao/', ReparticaoCreateView.as_view(), name='criar_reparticao'),
    path('reparticao/<int:pk>/editar/', ReparticaoUpdateView.as_view(), name='editar_reparticao'),
    path('reparticao/<int:pk>/deletar/', ReparticaoDeleteView.as_view(), name='deletar_reparticao'),

    path('lista_municipios/', MunicipiosListView.as_view(), name='lista_municipios'),
    path('criar_municipio/', MunicipioCreateView.as_view(), name='criar_municipio'),
    path('municipio/<int:pk>/editar/', MunicipioUpdateView.as_view(), name='editar_municipio'),
    path('municipio/<int:pk>/deletar/', MunicipioDeleteView.as_view(), name='deletar_municipio'),

]