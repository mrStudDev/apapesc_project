from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import AssociadoModel, MunicipiosCircusnscricaoModel, ReparticaoModel
from .forms import AssociadoForm, AssociadoSearchForm, MunicipioForm, ReparticaoForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from app_documentos.models import Documento
from app_home.models import ApapescModel
from app_associados.utils import formatar_valor_brasileiro

class AssociadosListView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/lista_associados.html'
    context_object_name = 'associados'

    class Meta:
        ordering = ['nome_completo']

    def get_queryset(self):
        return AssociadoModel.objects.filter(status="Associado Lista Ativo(a)")

class AssociadoDetailView(LoginRequiredMixin, DetailView):
    model = AssociadoModel
    template_name = 'app_associados/detail_associado.html'
    context_object_name = 'associado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        associado = self.object
        context['reparticao'] = self.object.reparticao
        context['documentos'] = Documento.objects.filter(associado=self.object)
        context['apapesc'] = ApapescModel.objects.first()  # Busca a única instância de ApapescModel
        context['quantidade1'] = formatar_valor_brasileiro(associado.quantidade1)
        context['quantidade2'] = formatar_valor_brasileiro(associado.quantidade2)
        context['quantidade3'] = formatar_valor_brasileiro(associado.quantidade3)
        context['quantidade4'] = formatar_valor_brasileiro(associado.quantidade4)
        context['quantidade5'] = formatar_valor_brasileiro(associado.quantidade5)

        return context


class AssociadoCreateView(LoginRequiredMixin, CreateView):
    model = AssociadoModel
    form_class = AssociadoForm
    template_name = 'app_associados/cadastrar_associado.html'

    def form_valid(self, form):
        # Salva o objeto
        self.object = form.save()

        # Verifica qual botão foi clicado
        if "save_and_continue" in self.request.POST:
            # Redireciona para a página de edição
            return redirect('app_associados:editar_associado', pk=self.object.pk)

        if "save_and_view" in self.request.POST:
            # Redireciona para a página de detalhe
            return redirect('app_associados:detalhe_associado', pk=self.object.pk)

        # Comportamento padrão (caso necessário)
        return super().form_valid(form)

    def get_success_url(self):
        # Redireciona para a página de detalhe por padrão
        return reverse_lazy('app_associados:detalhe_associado', kwargs={'pk': self.object.pk})


class AssociadoUpdateView(LoginRequiredMixin, UpdateView):
    model = AssociadoModel
    form_class = AssociadoForm
    template_name = 'app_associados/editar_associado.html'
    context_object_name = 'associado'

    def form_valid(self, form):
        # Salva o objeto
        self.object = form.save()

        # Verifica qual botão foi clicado
        if "save_and_continue" in self.request.POST:
            # Permite continuar editando na mesma página
            return redirect('app_associados:editar_associado', pk=self.object.pk)

        if "save_and_view" in self.request.POST:
            # Redireciona para a página de detalhe
            return redirect('app_associados:detalhe_associado', pk=self.object.pk)

        # Comportamento padrão (caso necessário)
        return super().form_valid(form)

    def get_success_url(self):
        # Redireciona para a página de detalhe por padrão
        return reverse_lazy('app_associados:detalhe_associado', kwargs={'pk': self.object.pk})



class AssociadoDeleteView(LoginRequiredMixin, DeleteView):
    model = AssociadoModel
    template_name = 'app_associados/delete_associado.html'
    context_object_name = 'associado'
    success_url = reverse_lazy('app_associados:lista_associados')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        associado_nome = self.object.nome_completo  # Captura o nome antes de excluir
        associado_id = self.object.pk  # Opcional, para referência
        self.object.delete()

        return render(request, self.template_name, {
            'deleted': True,
            'associado_nome': associado_nome,  # Passa o nome para exibir na mensagem
            'associado_id': associado_id,
        })


class AssociadoAposentadoListView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/aposentados.html'
    context_object_name = 'object_list'

    class Meta:
        ordering = ['nome_completo']

    def get_queryset(self):
        return AssociadoModel.objects.filter(status="Associado Lista Aposentado(a)")


class AssociadoSearchView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/buscar_associado.html'
    context_object_name = 'resultados'
    paginate_by = 1000

    def get_queryset(self):
        queryset = AssociadoModel.objects.none()  # Define como vazio inicialmente
        form = self.get_form()
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = AssociadoModel.objects.filter(
                    Q(nome_completo__icontains=query) |
                    Q(cpf__icontains=query) |
                    Q(celular__icontains=query)
                )
        return queryset

    def get_form(self):
        return AssociadoSearchForm(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class DesassociadosListView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/lista_desassociados.html'
    context_object_name = 'associados'

    class Meta:
        ordering = ['nome_completo']

    def get_queryset(self):
        return AssociadoModel.objects.filter(status="Desassociado(a)")

class ClientesEspeciaisListView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/lista_clientes_especiais.html'
    context_object_name = 'associados'

    class Meta:
        ordering = ['nome_completo']

    def get_queryset(self):
        return AssociadoModel.objects.filter(status="Cliente Especial")

class CandidatosListView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/lista_candidatos.html'
    context_object_name = 'associados'

    class Meta:
        ordering = ['nome_completo']

    def get_queryset(self):
        return AssociadoModel.objects.filter(status="Candidato(a)")



# Views para Repartição
class ReparticaoListView(LoginRequiredMixin, ListView):
    model = ReparticaoModel
    template_name = 'app_associados/lista_reparticoes.html'  # Crie este template
    context_object_name = 'reparticoes'


class ReparticaoCreateView(LoginRequiredMixin, CreateView):
    model = ReparticaoModel
    form_class = ReparticaoForm
    template_name = 'app_associados/criar_reparticao.html'  # Substitua pelo nome do seu template

    def form_valid(self, form):
        # Salva o objeto
        self.object = form.save()

        # Verifica qual botão foi clicado
        if "save_and_continue" in self.request.POST:
            # Redireciona para a mesma página de edição
            return redirect('app_associados:editar_reparticao', pk=self.object.pk)

        # Caso contrário, redireciona para a página de detalhe
        return super().form_valid(form)

    def get_success_url(self):
        # URL de sucesso padrão para redirecionar ao detalhe
        return reverse_lazy('app_associados:detail_reparticao', kwargs={'pk': self.object.pk})


class ReparticaoDetailView(LoginRequiredMixin, DetailView):
    model = ReparticaoModel
    template_name = 'app_associados/detail_reparticao.html'  # Defina o caminho do template para a página de detalhes
    context_object_name = 'reparticao'

class ReparticaoUpdateView(LoginRequiredMixin, UpdateView):
    model = ReparticaoModel
    form_class = ReparticaoForm
    template_name = 'app_associados/editar_reparticao.html'  # Template para edição
    success_url = reverse_lazy('app_associados:lista_reparticoes')  # URL de redirecionamento após edição

    def form_valid(self, form):
        # Salva o objeto
        self.object = form.save()

        # Verifica qual botão foi clicado
        if "save_and_continue" in self.request.POST:
            # Redireciona para a mesma página de edição
            return redirect('app_associados:editar_reparticao', pk=self.object.pk)

        # Caso contrário, redireciona para a página de detalhe
        return super().form_valid(form)

    def get_success_url(self):
        # URL de sucesso padrão para redirecionar ao detalhe
        return reverse_lazy('app_associados:detail_reparticao', kwargs={'pk': self.object.pk})


class ReparticaoDeleteView(LoginRequiredMixin, DeleteView):
    model = ReparticaoModel
    template_name = 'app_associados/deletar_reparticao.html'  # Template para confirmação de exclusão
    success_url = reverse_lazy('app_associados:lista_reparticoes')  # URL de redirecionamento após exclusão



# Views para Municipios
class MunicipiosListView(LoginRequiredMixin, ListView):
    model = MunicipiosCircusnscricaoModel
    template_name = 'app_associados/lista_municipios.html'
    context_object_name = 'municipios'

    def get_queryset(self):
        return MunicipiosCircusnscricaoModel.objects.order_by('municipio')  # Ordena em ordem alfabética

class MunicipioCreateView(LoginRequiredMixin, CreateView):
    model = MunicipiosCircusnscricaoModel
    form_class = MunicipioForm
    template_name = 'app_associados/criar_municipio_circunscricao.html'  # Substitua pelo nome do seu template
    success_url = reverse_lazy('app_associados:lista_municipios') # Defina a URL para onde redirecionar após a criação


class MunicipioUpdateView(LoginRequiredMixin, UpdateView):
    model = MunicipiosCircusnscricaoModel
    form_class = MunicipioForm
    template_name = 'app_associados/editar_municipio_circunscricao.html'  # Template para edição
    success_url = reverse_lazy('app_associados:lista_municipios')  # URL de redirecionamento após edição

class MunicipioDeleteView(LoginRequiredMixin, DeleteView):
    model = MunicipiosCircusnscricaoModel
    template_name = 'app_associados/deletar_municipio_circunscricao.html'  # Template para confirmação de exclusão
    success_url = reverse_lazy('app_associados:lista_municipios')  # URL de redirecionamento após exclusão

