from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import DocumentoForm
from .models import Documento
from app_associados.models import AssociadoModel
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from reportlab.pdfgen import canvas
from .models import Documento
from PIL import Image
from reportlab.lib.pagesizes import letter
import os
import io
from django.http import JsonResponse
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from docx import Document
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from .models import Documento
from docx2pdf import convert
from django.conf import settings
import subprocess


class DocumentoUploadView(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'app_documentos/upload_documento.html'

    def dispatch(self, request, *args, **kwargs):
        self.associado_id = kwargs.get('associado_id')
        self.associado = get_object_or_404(AssociadoModel, id=self.associado_id)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.associado = self.associado
        return super().form_valid(form)

    def get_success_url(self):
        # Redireciona para o detalhe do documento recém-criado
        return reverse('app_documentos:documento_detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['associado'] = self.associado
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['associado'] = self.associado
        return context


# View para listar documentos
class DocumentoListView(ListView):
    model = Documento
    template_name = 'documentos/documentos_list.html'
    context_object_name = 'documentos'

    def get_queryset(self):
        return Documento.objects.select_related('associado').all()


# View para detalhes do documento
class DocumentoDetailView(DetailView):
    model = Documento
    template_name = 'app_documentos/documento_detail.html'
    context_object_name = 'documento'


class DocumentoDeleteView(View):
    def post(self, request, pk):
        try:
            documento = Documento.objects.get(pk=pk)
            documento.delete()
            return JsonResponse({'success': True, 'message': 'Documento excluído com sucesso.'})
        except Documento.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Documento não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Erro: {str(e)}'}, status=500)



@csrf_exempt
def criar_copia_pdf(request, pk):
    try:
        documento = Documento.objects.get(pk=pk)
        associado = documento.associado

        # Nome do PDF
        pdf_name = f"{documento.tipo_doc.replace(' ', '_')}_{associado.nome_completo.replace(' ', '_')}_copia.pdf"
        pdf_path = os.path.join(settings.MEDIA_ROOT, "documentos", pdf_name)

        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

        # Lógica para arquivos de imagem
        if documento.arquivo.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer, pagesize=A4)
            a4_width, a4_height = A4

            with Image.open(documento.arquivo.path) as img:
                img_width, img_height = img.size
                aspect_ratio = img_width / img_height

                # Calcula o tamanho da imagem para caber na página A4 com margens
                margin = 50  # Margem de 50 unidades em todos os lados
                max_width = a4_width - 2 * margin
                max_height = a4_height - 2 * margin

                if aspect_ratio > 1:
                    width = min(max_width, img_width)
                    height = width / aspect_ratio
                else:
                    height = min(max_height, img_height)
                    width = height * aspect_ratio

                # Ajusta se exceder o tamanho máximo permitido
                if width > max_width:
                    width = max_width
                    height = width / aspect_ratio
                if height > max_height:
                    height = max_height
                    width = height * aspect_ratio

                x = (a4_width - width) / 2  # Centraliza horizontalmente
                y = (a4_height - height) / 2  # Centraliza verticalmente

                p.drawImage(documento.arquivo.path, x, y, width=width, height=height)

            p.showPage()
            p.save()

            # Salva o PDF no disco
            buffer.seek(0)
            with open(pdf_path, 'wb') as f:
                f.write(buffer.read())

        # Lógica para arquivos DOCX
        elif documento.arquivo.name.lower().endswith('.docx'):
            # Caminho completo do arquivo DOCX
            docx_path = documento.arquivo.path

            # Comando para converter o DOCX para PDF usando o LibreOffice
            command = [
                'libreoffice',
                '--headless',
                '--convert-to', 'pdf',
                '--outdir', os.path.dirname(pdf_path),
                docx_path
            ]

            # Executa o comando
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Verifica se a conversão foi bem-sucedida
            if result.returncode != 0:
                return JsonResponse({'success': False, 'message': f'Erro na conversão do documento: {result.stderr.decode("utf-8")}'})

            # O LibreOffice salva o PDF com o mesmo nome do arquivo DOCX, mas com extensão .pdf
            original_pdf_name = os.path.splitext(os.path.basename(docx_path))[0] + '.pdf'
            original_pdf_path = os.path.join(os.path.dirname(pdf_path), original_pdf_name)

            # Renomeia o PDF para o nome desejado
            os.rename(original_pdf_path, pdf_path)

        else:
            return JsonResponse({'success': False, 'message': 'Formato de arquivo não suportado.'})

        # Salva o PDF no banco de dados
        documento_copia = Documento.objects.create(
            associado=associado,
            tipo_doc=documento.tipo_doc,
            nome=f"Cópia - {documento.nome}",
            arquivo=f"documentos/{pdf_name}",
            descricao=f"Cópia PDF - Documento gerado automaticamente - {documento.nome}"
        )

        return JsonResponse({'success': True, 'message': 'Cópia do documento criada com sucesso!'})

    except Documento.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Documento não encontrado.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Erro: {str(e)}'})