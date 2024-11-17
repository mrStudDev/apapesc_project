from django.contrib.staticfiles import finders
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from pdfrw import PdfReader, PdfWriter, PageMerge
from datetime import datetime
from io import BytesIO
from app_associados.models import AssociadoModel
from app_home.models import ApapescModel
import os
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from urllib.parse import urlencode
from django.urls import reverse
from django.shortcuts import get_object_or_404
from reportlab.lib.colors import Color, HexColor, lightgrey
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


# PÁGINA DE AÇÕES -  AS AÇÕES GERAR ESTÃO VÍNCULADAS NESSA PÁGINA
def pagina_acoes(request, associado_id=None):
    pdf_url = request.GET.get('pdf_url')
    if not pdf_url:
        return HttpResponse("URL do PDF não encontrada.", status=400)

    associado = None
    if associado_id:
        associado = get_object_or_404(AssociadoModel, pk=associado_id)

    apapesc = ApapescModel.objects.first()
    if not apapesc:
        return HttpResponse("Informações da APAPESC não estão configuradas.", status=404)

    return render(request, 'app_automacoes/pagina_acoes.html', {
        'pdf_url': pdf_url,
        'associado': associado,
        'apapesc': apapesc,
    })


# GERAR DECLARAÇÃO DE FILIADO
def gerar_declaracao_filiado(request, associado_id):
    associado = AssociadoModel.objects.get(id=associado_id)
    # Obtém a primeira instância de ApapescModel
    apapesc = ApapescModel.objects.first()
    if not apapesc:
        return HttpResponse("Informações da APAPESC não estão configuradas.", status=404)

    # Caminho para o PDF de template
    template_path = finders.find('pdf/modelo_declaracao_filiacao.pdf')
    template_pdf = PdfReader(template_path)
    template_page = template_pdf.pages[0]  # Primeira página como template

    # Buffer para gerar o PDF dinamicamente
    buffer = BytesIO()

    # Estilos personalizados
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(
        'Title',
            parent=styles['Title'],
            fontName='Times-Bold',
            fontSize=11,
            alignment=2,
            leading=32,  # Define a altura da linha
            spaceBefore=100,  # Espaçamento antes do parágrafo
            textColor=lightgrey,
    )

    style_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=22,  # Espaçamento entre as linhas
        alignment=4
    )

    style_veracidade = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=18,  # Espaçamento entre as linhas
        alignment=4,
        leftIndent=50,  # Indenta o texto para a direita
    )

    style_data = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=18,  # Espaçamento entre as linhas
        spaceBefore=10,
        alignment=4
    )

    style_assinatura = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=18,  # Espaçamento entre as linhas
        alignment=4
    )

    # Data atual
    data_atual = datetime.now().strftime('%d/%m/%Y')

    # Texto da declaração
    texto = (
        f"A APAPESC, ASSOCIAÇÃO DOS PESCADORES ARTESANAIS E PROFISSIONAIS DO ESTADO DE SANTA CATARINA, "
        f"inscrita no CNPJ sob o nº 48.719703/0001-09, com sede à RUA FERNANDO MACHADO, n° 73, 3° ANDAR "
        f"SALA 302, CENTRO, FLORIANÓPOLIS-SC, declara para os devidos fins que "
        f"<strong>{associado.nome_completo},</strong> inscrito no CPF sob o nº {associado.cpf} e no RG nº "
        f"{associado.rg_numero} - {associado.rg_orgao}, é filiado(a) a esta entidade desde "
        f"{associado.data_cadastro.strftime('%d/%m/%Y')}."
    )

    local_data = f"FLORIANÓPOLIS, {data_atual}."

    assinatura = (
        '_________________________________________________________________________<br/>'
        "SAMARA IZILDA CORREA DOS SANTOS<br/>"
        "PROCURADORA APAPESC<br/>"
        "ASSOCIAÇÃO DOS PESCADORES ARTESANAIS E PROFISSIONAIS DO ESTADO DE SANTA CATARINA"
        f"<br/>Presidente: {apapesc.presidente}"
    )

    declaracao_veracidade = (
        "<strong>Declaro sob as penas de lei (Art. 299 do Código Penal) a veracidade das informações "
        "aqui prestadas para emissão desta declaração, ficando sob minha responsabilidade as "
        "informações nelas contidas e eventuais informações não declaradas.</strong>"
    )

    # Criação do Frame para controlar margens e posicionamento
    pdf_canvas = Frame(x1=75, y1=75, width=450, height=700, showBoundary=1)

    # Adiciona o título, texto, local e assinatura ao Frame
    elements = [
        Paragraph("Apapesc - Promevento a pesca legal e equilíbrio ambiental em SC", style_title),
        Spacer(1, 90),

        Paragraph(texto, style_normal),
        Spacer(1, 14),

        Paragraph(declaracao_veracidade, style_veracidade),
        Spacer(1, 18),

        Paragraph(local_data, style_data),
        Spacer(1, 24),

        Paragraph(assinatura, style_assinatura),
        Spacer(1, 16),

    ]

    # Gerando o conteúdo dinâmico
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=68, leftMargin=68, topMargin=172, bottomMargin=50)
    doc.build(elements)

    # Mesclando o conteúdo dinâmico com o template
    buffer.seek(0)
    overlay_pdf = PdfReader(buffer)
    overlay_page = overlay_pdf.pages[0]

    merger = PageMerge(template_page)
    merger.add(overlay_page).render()

    # Salvando o PDF mesclado no sistema de arquivos
    pdf_name = f"declaracao_filiado_{associado_id}_{associado.nome_completo.replace(' ', '_')}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'documentos', pdf_name)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    PdfWriter(pdf_path, trailer=template_pdf).write()

    # Redirecionando para a página de ações com o URL do PDF
    pdf_url = f"{settings.MEDIA_URL}documentos/{pdf_name}"
    query_string = urlencode({'pdf_url': pdf_url})
    redirect_url = f"{reverse('app_automacoes:pagina_acoes', args=[associado.id])}?{query_string}"
    return redirect(redirect_url)


# GERAR DECLARAÇÃO DE ATIVIDADE PESQUEIRA
def gerar_declaracao_atividade_pesqueira(request, associado_id):
    associado = AssociadoModel.objects.get(id=associado_id)

    # Obtém a primeira instância de ApapescModel
    apapesc = ApapescModel.objects.first()
    if not apapesc:
        return HttpResponse("Informações da APAPESC não estão configuradas.", status=404)

    # Caminho para o PDF de template
    template_path = finders.find('pdf/modelo_atividade_pesqueira.pdf')
    template_pdf = PdfReader(template_path)
    template_page = template_pdf.pages[0]  # Primeira página como template

    # Buffer para gerar o PDF dinamicamente
    buffer = BytesIO()

    # Estilos personalizados
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontName='Times-Bold',
        fontSize=11,
        alignment=2,
        leading=32,  # Espaçamento entre as linhas do título
        spaceBefore=100,  # Espaçamento antes do título
        textColor=colors.grey,
    )

    style_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=15,  # Espaçamento entre as linhas do texto
        alignment=4,  # Justificado
    )

    # Data atual
    data_atual = datetime.now().strftime('%d/%m/%Y')

    # Texto inicial da declaração
    texto = (
        f"A Associação dos Pescadores Artesanais e Profissionais do Estado de Santa Catarina (APAPESC), "
        f"inscrita no CNPJ sob n° 48.719703/0001-09, com sede na Rua Fernando Machado, n° 73, sala 302, "
        f"Centro, Florianópolis/SC, representada neste ato por seu presidente, Peterson da Conceição Domingues, "
        f"brasileiro, casado, portador da carteira de identidade n° 7.546.341 - SSP/SC, inscrito no CPF sob n° "
        f"109.707.649-01, Residente e domiciliado na Avenida Engenheiro Max de Souza , n° 1655, Coqueiros, "
        f"Florianópolis - SC, CEP 88080-000, declara que o Sr(a). <strong>{associado.nome_completo},</strong> "
        f"inscrito no CPF sob o nº {associado.cpf}, é pescador registrado no Ministério da Agricultura, "
        f"Pesca e Abastecimento (MAPA), sob o nº {associado.rgp}, é residente e domiciliado(a) na {associado.logradouro}, "
        f"nº {associado.numero}, {associado.complemento}, {associado.bairro} {associado.municipio}, {associado.cep}, "
        f"dedica-se à pesca artesanal profissional, com meios de produção próprios ou em regime de parceria com outros "
        f"pescadores artesanais e que sua renda depende de sua produção."
    )

    local_data = f"FLORIANÓPOLIS, {data_atual}."

    # Dados para a tabela
    dados_tabela = [
        ["ESPÉCIE", "QUANTIDADE MÉDIA ANUAL (Kg)"],  # Cabeçalho da tabela
        [associado.especie1, associado.quantidade1],
        [associado.especie2, associado.quantidade2],
        [associado.especie3, associado.quantidade3],
        [associado.especie4, associado.quantidade4],
        [associado.especie5, associado.quantidade5],
    ]

    # Criação da tabela
    tabela = Table(dados_tabela, colWidths=[200, 200])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    assinatura = (
        "Por ser verdade, firmo e dou Fé.<br/><br/><br/>"
        "__________________________________________________________________________<br/>"
        "Jurídico Samara Santos | OAB/SC: 51380<br/>"        
        f"Presidente da Associação: {apapesc.presidente}"

    )

    # Elementos para o PDF
    elements = [
        Paragraph("Apapesc - Promoção da pesca legal e equilíbrio ambiental em SC", style_title),
        Spacer(1, 100),
        Paragraph(texto, style_normal),
        Spacer(1, 17),
        tabela,  # Adicionando a tabela ao PDF
        Spacer(1, 15),
        Paragraph(local_data, style_normal),
        Spacer(1, 10),
        Paragraph(assinatura, style_normal),
    ]

    # Gerando o conteúdo dinâmico
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=172, bottomMargin=50)
    doc.build(elements)

    # Mesclando o conteúdo dinâmico com o template
    buffer.seek(0)
    overlay_pdf = PdfReader(buffer)
    overlay_page = overlay_pdf.pages[0]

    merger = PageMerge(template_page)
    merger.add(overlay_page).render()

    # Salvando o PDF no disco
    pdf_name = f"declaracao_atividade_pesqueira_{associado_id}_{associado.nome_completo.replace(' ', '_')}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'documentos', pdf_name)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    PdfWriter(pdf_path, trailer=template_pdf).write()

    # Redirecionando para a página de ações
    pdf_url = f"{settings.MEDIA_URL}documentos/{pdf_name}"
    query_string = urlencode({'pdf_url': pdf_url})
    redirect_url = f"{reverse('app_automacoes:pagina_acoes', args=[associado.id])}?{query_string}"
    return redirect(redirect_url)


# GERAR DECLARAÇÃO DE RESIDÊNCIA
def gerar_declaracao_residencia(request, associado_id):
    associado = AssociadoModel.objects.get(id=associado_id)

    # Caminho para o PDF de template
    template_path = finders.find('pdf/modelo_formal_residencia.pdf')
    template_pdf = PdfReader(template_path)
    template_page = template_pdf.pages[0]  # Primeira página como template

    # Buffer em memória para o conteúdo dinâmico
    buffer = BytesIO()

    # Definindo estilos personalizados
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontName='Times-Bold',
        fontSize=16,
        alignment=1,  # Centralizado
        leading=32,  # Espaçamento entre as linhas do título
        spaceBefore=100,  # Espaçamento antes do título
        textColor=colors.grey,
    )
    style_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=28,  # Espaçamento entre linhas
        alignment=4,  # Justificado
    )
    style_assinatura = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=28,  # Espaçamento entre linhas
        alignment=1,  # Centralizado
    )
    style_data = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=28,  # Espaçamento entre linhas
        alignment=0,  # Esquerda
        spaceBefore=20,  # Espaçamento antes do título
    )
    # Data atual
    data_atual = datetime.now().strftime('%d/%m/%Y')

    # Texto da declaração
    texto = (
        f"Eu, <strong>{associado.nome_completo}</strong>, inscrito no CPF nº {associado.cpf}, na falta de documentos "
        f"para comprovação de residência, em conformidade com o disposto na Lei 7.115, de 29 de "
        f"agosto de 1983, DECLARO para os devidos fins, sob penas da Lei, que RESIDO no endereço: "
        f"<strong>{associado.logradouro}, nº {associado.numero}, {associado.complemento},"
        f" {associado.bairro}, {associado.municipio} - {associado.uf} {associado.cep}.</strong>"
    )

    # Declaração de veracidade
    declaracao_veracidade = (
        "Declaro sob as penas da lei (Art. 299 do Código Penal) a veracidade das informações "
        "aqui prestadas para emissão desta declaração, ficando sob minha responsabilidade as "
        "informações nelas contidas e eventuais informações não declaradas."
    )

    # Local e data
    local_data = f"FLORIANÓPOLIS, {data_atual}."

    # Assinatura
    assinatura = (
        "____________________________________________________________________<br/>"
        f"{associado.nome_completo} - CPF: {associado.cpf}<br/>"
    )

    # Elementos do PDF na ordem correta
    elements = [
        Paragraph("DECLARAÇÃO DE RESIDÊNCIA", style_title),
        Spacer(1, 20),
        Paragraph(texto, style_normal),
        Spacer(1, 10),
        Paragraph(declaracao_veracidade, style_normal),
        Paragraph(local_data, style_data),
        Spacer(1, 24),
        Paragraph(assinatura, style_assinatura),
        Spacer(1, 26),
    ]

    # Criação do documento PDF
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=85,
        leftMargin=85,
        topMargin=160,
        bottomMargin=40,
    )

    # Gerar o conteúdo do PDF
    doc.build(elements)

    # Mesclar o conteúdo dinâmico com o template PDF
    buffer.seek(0)
    overlay_pdf = PdfReader(buffer)
    overlay_page = overlay_pdf.pages[0]

    merger = PageMerge(template_page)
    merger.add(overlay_page).render()

    # Salvar o PDF em disco
    pdf_name = f"declaracao_residencia_{associado.nome_completo.replace(' ', '_')}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'documentos', pdf_name)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    PdfWriter(pdf_path, trailer=template_pdf).write()

    # Construir o URL para o PDF
    pdf_url = f"{settings.MEDIA_URL}documentos/{pdf_name}"

    # Redirecionar para a página de ações
    query_string = urlencode({'pdf_url': pdf_url})
    redirect_url = f"{reverse('app_automacoes:pagina_acoes', kwargs={'associado_id': associado.id})}?{query_string}"
    return redirect(redirect_url)



# DECLARAÇÃO DE HIPOSSUFICIÊNCIA
def gerar_declaracao_hipo(request, associado_id):
    associado = AssociadoModel.objects.get(id=associado_id)

    # Caminho para o PDF de template
    template_path = finders.find('pdf/modelo_hipo.pdf')
    template_pdf = PdfReader(template_path)
    template_page = template_pdf.pages[0]  # Primeira página como template

    # Buffer em memória para o conteúdo dinâmico
    buffer = BytesIO()

    # Definindo estilos personalizados
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontName='Times-Bold',
        fontSize=16,
        alignment=1,  # Centralizado
        leading=32,  # Espaçamento entre as linhas do título
        spaceBefore=100,  # Espaçamento antes do título
        textColor=colors.grey,
    )
    style_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=22,  # Espaçamento entre linhas
        alignment=4,  # Justificado
    )
    style_assinatura = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=28,  # Espaçamento entre linhas
        alignment=1,  # Centralizado
    )
    style_data = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=28,  # Espaçamento entre linhas
        alignment=0,  # Esquerda
        spaceBefore=50,  # Espaçamento antes do título
    )
    style_veracidade = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=18,  # Espaçamento entre as linhas
        alignment=4,
        leftIndent=50,  # Indenta o texto para a direita
    )

    # Data atual
    data_atual = datetime.now().strftime('%d/%m/%Y')

    # Texto da declaração
    texto = (
        f"Eu, <strong>{associado.nome_completo}</strong>, profissão {associado.profissao}, "
        f"estado civil {associado.estado_civil}, inscrito(a) no CPF nº {associado.cpf}, e RG: nº{associado.rg_numero}, "
        f"com domicílio e residência estabelecido à {associado.logradouro}, nº {associado.numero}, {associado.complemento}, {associado.bairro}, "
        f"{associado.municipio} - {associado.uf} {associado.cep}. <strong>DECLARO</strong>, para todos os fins de "
        f"direito e sob as penas da lei, que não tenho condições de arcar com as despesas inerentes ao presente "
        f"processo, sem prejuízo do meu sustento e de minha família, necessitando, portanto, da "
        f"<strong>GRATUIDADE DA JUSTIÇA</strong>, nos termos do art. 98 e seguintes da Lei 13.105/2015 "
        f"(Código de Processo Civil). Requeiro, ainda, que o benefício abarque todos os atos do processo."
    )

    # Declaração de veracidade
    declaracao_veracidade = (
        "<strong>Declaro sob as penas da lei (Art. 299 do Código Penal) a veracidade das informações "
        "aqui prestadas para emissão desta declaração, ficando sob minha responsabilidade as "
        "informações nelas contidas e eventuais informações não declaradas.</strong>"
    )

    # Local e data
    local_data = f"FLORIANÓPOLIS, {data_atual}."

    # Assinatura
    assinatura = (
        "____________________________________________________________________<br/>"
        f"{associado.nome_completo} - CPF: {associado.cpf}<br/>"
    )

    # Elementos do PDF na ordem correta
    elements = [
        Paragraph("DECLARAÇÃO DE HIPOSSUFICIÊNCIA", style_title),
        Spacer(1, 20),
        Paragraph(texto, style_normal),
        Spacer(1, 10),
        Paragraph(declaracao_veracidade, style_veracidade),
        Paragraph(local_data, style_data),
        Spacer(1, 14),
        Paragraph(assinatura, style_assinatura),
        Spacer(1, 26),
    ]

    # Criação do documento PDF
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=85,
        leftMargin=85,
        topMargin=160,
        bottomMargin=40
    )

    # Gerar o conteúdo do PDF
    doc.build(elements)

    # Mesclar o conteúdo dinâmico com o template PDF
    buffer.seek(0)
    overlay_pdf = PdfReader(buffer)
    overlay_page = overlay_pdf.pages[0]

    merger = PageMerge(template_page)
    merger.add(overlay_page).render()

    # Salvar o PDF no disco
    pdf_name = f"declaracao_hipo_{associado.nome_completo.replace(' ', '_')}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'documentos', pdf_name)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    PdfWriter(pdf_path, trailer=template_pdf).write()

    # Construir o URL do PDF
    pdf_url = f"{settings.MEDIA_URL}documentos/{pdf_name}"

    # Redirecionar para a página de ações com o URL do PDF
    query_string = urlencode({'pdf_url': pdf_url})
    redirect_url = f"{reverse('app_automacoes:pagina_acoes', kwargs={'associado_id': associado.id})}?{query_string}"
    return redirect(redirect_url)



# GERAR PROCURAÇÃO AD JUDICIA
def gerar_procuracao_juridica(request, associado_id):
    associado = AssociadoModel.objects.get(id=associado_id)

    # Caminho para o PDF de template
    template_path = finders.find('pdf/modelo_procuracao.pdf')
    template_pdf = PdfReader(template_path)

    # Buffer em memória para o conteúdo dinâmico
    buffer = BytesIO()

    # Definindo estilos personalizados
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontName='Times-Bold',
        fontSize=17,
        alignment=1,  # Centralizado
        leading=32,  # Espaçamento entre as linhas do título
        spaceBefore=100,  # Espaçamento antes do título
    )
    style_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=14,  # Espaçamento entre linhas
        alignment=4,  # Justificado
    )
    style_assinatura = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=14,  # Espaçamento entre linhas
        alignment=1,  # Justificado
    )
    # Data atual
    data_atual = datetime.now().strftime('%d/%m/%Y')

    # Texto da declaração
    texto1 = (
        f"<strong>OUTORGANTE(S)</strong>: <strong>{associado.nome_completo}</strong>, brasileira, "
        f"profissão, {associado.profissao}, estado civil, {associado.estado_civil}, CPF nº {associado.cpf}, "
        f"RG nº {associado.rg_numero}, com residência e domicílio estabelecido á {associado.logradouro}, "
        f"nº {associado.numero}, {associado.complemento}, {associado.bairro}, {associado.municipio} -"
        f" {associado.uf} {associado.cep}. "
        f"<br /><br /><strong>OUTORGADOS</strong>: <strong>CRISTIANI JORDANI DOS SANTOS RAMOS</strong>, "
        f"brasileira, casada, advogada, inscrição na OAB/SC sob o número 51.410, inscrita no CPF 853.801.219-34, "
        f"<strong>SAMARA IZILDA CORREA DOS SANTOS</strong>,  brasileira, divorciada,"
        f"advogada, inscrição na OAB/SC sob o número 51.380, inscrita no CPF 027.034.419-59, integrantes do "
        f"escritório JORDANI & SANTOS Advogados Associados."
    )
    texto2 =(
        f"<strong>PODERES:</strong> Nos termos do art. 105 do CPC para o foro em geral, conferindo-lhe os mais amplos"
        f" e ilimitados poderes inclusive os da cláusula “ad judicia et extra”, para, onde com esta se apresentar, "
        f"em conjunto ou separadamente, independente de ordem de nomeação, propor ações e contestá-las, receber "
        f"citações, notificações e intimações, apresentar justificações, variar de ações e pedidos, notificar, "
        f"interpelar, protestar, discordar, transigir e desistir, receber a quantia e dar quitação, arrematar "
        f"ou adjudicar em qualquer praça ou leilão, reter dos valores finais auferidos na demanda,  honorários "
        f"contratuais de 30% e também o valor equivalente a três benefícios estabelecidos em sentença, prestar "
        f"compromissos de inventariante, oferecer as primeiras e últimas declarações, interpor quaisquer recursos, "
        f"requerer, assinar, praticar, perante qualquer repartição pública, entidades autárquicas e ou parestatal, "
        f"Juízo, Instância ou Tribunal, tudo o que julgar conveniente ou necessário ao bom e fiel desempenho deste "
        f"mandato, que poderá ser substabelecido, no todo ou em parte, a quem melhor lhe convier, com ou sem reserva "
        f"de poderes, EM ESPECIAL PARA PROPOR AÇÃO JUDICIAL DE APOSENTADORIA BEM COMO, POR FORÇA DO ARTIGO 661 DO "
        f"Código Civil, PRESTAR OU ASSINAR DECLARAÇÃO DE ISENÇÃO DO IMPOSTO DE RENDA."
    )

    # Local e data
    local_data = f"FLORIANÓPOLIS, {data_atual}."
    assinatura = (
        "____________________________________________________________________<br/>"
        f"<strong>{associado.nome_completo}</strong><br/>"
        f"CPF: {associado.cpf}<br/>"
    )

    # Elementos do PDF
    elements = [
        Paragraph("PROCURAÇÃO AD JUDICIA", style_title),
        Spacer(1, 10),
        Paragraph(texto1, style_normal),
        Spacer(1, 10),
        Paragraph(texto2, style_normal),
        Spacer(1, 10),
        Paragraph(local_data, style_normal),
        Spacer(1, 24),
        Paragraph(assinatura, style_assinatura),
    ]

    # Criando o documento PDF
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=85,
        leftMargin=85,
        topMargin=140,
        bottomMargin=40,
    )

    doc.build(elements)

    # Mesclando o conteúdo dinâmico com o template
    buffer.seek(0)
    overlay_pdf = PdfReader(buffer)

    # **Ajuste Importante:**
    # O número de páginas do template e o overlay_pdf deve ser gerenciado com cuidado.
    for index, template_page in enumerate(template_pdf.pages):
        if index < len(overlay_pdf.pages):
            overlay_page = overlay_pdf.pages[index]
            PageMerge(template_page).add(overlay_page).render()

    # Salvando o PDF final
    pdf_name = f"procuracao_juridica_{associado.nome_completo.replace(' ', '_')}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'documentos', pdf_name)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    PdfWriter(pdf_path, trailer=template_pdf).write()

    # Preparando o redirecionamento
    pdf_url = f"{settings.MEDIA_URL}documentos/{pdf_name}"
    return redirect(f"{reverse('app_automacoes:pagina_acoes', args=[associado.id])}?pdf_url={pdf_url}")



# GERAR CERTIFICADO DE REGISTRO
def gerar_certificado(request, associado_id):
    associado = AssociadoModel.objects.get(id=associado_id)

    # Carregar o template PDF
    template_path = finders.find('pdf/back_certificado.pdf')
    template_pdf = PdfReader(template_path)
    template_page = template_pdf.pages[0]

    # Buffer para o conteúdo dinâmico
    buffer = BytesIO()

    # Configuração do documento PDF no formato paisagem
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=200, leftMargin=90, topMargin=330, bottomMargin=40
    )

    # Definição de estilos personalizados
    styles = getSampleStyleSheet()
    style_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16,
        alignment=4  # Justificado
    )

    # Conteúdo do certificado
    texto = (
        f"Certificamos que <strong>{associado.nome_completo}</strong> é associado(a) à APAPESC "
        f"e exerce a profissão de Pescador(a) profissional, registrado(a) sob o RGP nº {associado.rgp}. "
        f"Com orgulho, reconhecemos sua dedicação ao ofício que sustenta tanto a economia quanto as "
        f"tradições culturais de Santa Catarina. A trajetória de cada associado(a) fortalece a comunidade pesqueira "
        f" e mantém viva nossa herança regional. A APAPESC valoriza e apoia os pescadores e pescadoras, reafirmando seu"
        f" compromisso com o desenvolvimento sustentável e a preservação dos costumes locais."
    )

    # Data e assinatura
    data_atual = datetime.now().strftime('%d / %M / %Y')
    local_data = f"FLORIANÓPOLIS, {data_atual}."
    assinatura = (
        "SAMARA IZILDA CORREA DOS SANTOS<br/>"
        "Procuradora <strong>APAPESC</strong><br/>"
        "Associação dos Pescadores Artesanais e Profissionais do Estado de Santa Catarina"
    )

    # Adicionando o conteúdo ao PDF
    elements = [
        Paragraph(texto, style_normal),
        Spacer(1, 10),
        Paragraph(local_data, style_normal),
        Spacer(1, 5),
        Paragraph(assinatura, style_normal),
    ]

    # Construindo o PDF diretamente
    doc.build(elements)

    # Mesclando o conteúdo dinâmico com o template PDF
    buffer.seek(0)
    overlay_pdf = PdfReader(buffer)
    overlay_page = overlay_pdf.pages[0]

    merger = PageMerge(template_page)
    merger.add(overlay_page).render()

    # Retornando o PDF final na resposta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificado_{associado.nome_completo}.pdf"'
    PdfWriter().write(response, template_pdf)

    return response

