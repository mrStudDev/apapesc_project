from django.urls import path
from .views import DocumentoUploadView, DocumentoListView, DocumentoDetailView, DocumentoDeleteView
from .views import criar_copia_pdf
app_name = 'app_documentos'

urlpatterns = [
    path('upload/<int:associado_id>/', DocumentoUploadView.as_view(), name='upload_documento'),  # Upload com associado

    path('list/', DocumentoListView.as_view(), name='documentos_list'),  # Lista de documentos
    path('detail/<int:pk>/', DocumentoDetailView.as_view(), name='documento_detail'),  # Detalhes do documento
    path('delete/<int:pk>/', DocumentoDeleteView.as_view(), name='delete_documento'),
    path('criar_pdf/<int:pk>/', criar_copia_pdf, name='criar_copia_pdf'),
]