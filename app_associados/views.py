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

class AssociadosListView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/lista_associados.html'
    context_object_name = 'associados'

    class Meta:
        ordering = ['nome_completo']

    def get_queryset(self):
        return AssociadoModel.objects.filter(status="Ativo(a)")

class AssociadoDetailView(LoginRequiredMixin, DetailView):
    model = AssociadoModel
    template_name = 'app_associados/detail_associado.html'
    context_object_name = 'associado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reparticao'] = self.object.reparticao
        return context


class AssociadoCreateView(LoginRequiredMixin, CreateView):
    model = AssociadoModel
    form_class = AssociadoForm
    template_name = 'app_associados/cadastrar_associado.html'
    success_url = reverse_lazy('app_associados:detalhe_associado')


    def form_valid(self, form):
        self.object = form.save()

        if "save_and_continue" in self.request.POST:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_associados:detalhe_associado', kwargs={'pk': self.object.pk})



class AssociadoUpdateView(LoginRequiredMixin, UpdateView):
    model = AssociadoModel
    form_class = AssociadoForm
    template_name = 'app_associados/editar_associado.html'  # Template onde o formulário de edição será renderizado
    success_url = reverse_lazy('app_associados:detalhe_associado')
    context_object_name = 'associado'


    def form_valid(self, form):
        self.object = form.save()

        if "save_and_continue" in self.request.POST:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_associados:detalhe_associado', kwargs={'pk': self.object.pk})



class AssociadoDeleteView(LoginRequiredMixin, DeleteView):
    model = AssociadoModel
    template_name = 'app_associados/delete_associado.html'
    context_object_name = 'associado'
    success_url = reverse_lazy('app_associados:lista_associados')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        associado_nome = self.object.nome  # Para usar no contexto, se necessário
        self.object.delete()
        return render(request, self.template_name, {
            'associado': self.object,
            'deleted': True,  # Indica que o objeto foi deletado
            'associado_nome': associado_nome,
        })

class AssociadoAposentadoListView(LoginRequiredMixin, ListView):
    model = AssociadoModel
    template_name = 'app_associados/aposentados.html'
    context_object_name = 'object_list'

    class Meta:
        ordering = ['nome_completo']

    def get_queryset(self):
        return AssociadoModel.objects.filter(status="Aposentado(a)")


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


# Views para Repartição
class ReparticaoListView(LoginRequiredMixin, ListView):
    model = ReparticaoModel
    template_name = 'app_associados/lista_reparticoes.html'  # Crie este template
    context_object_name = 'reparticoes'


class ReparticaoCreateView(LoginRequiredMixin, CreateView):
    model = ReparticaoModel
    form_class = ReparticaoForm
    template_name = 'app_associados/criar_reparticao.html'  # Substitua pelo nome do seu template

    def get_success_url(self):
        # Redireciona para a página de detalhes usando o `pk` do objeto recém-criado
        return reverse('app_associados:detail_reparticao', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Salva o objeto
        self.object = form.save()

        # Verifica se o botão "Salvar e Continuar" foi pressionado
        if "save_and_continue" in self.request.POST:
            # Recarrega a mesma página com os dados preenchidos no formulário
            return self.render_to_response(self.get_context_data(form=form))

        # Caso contrário, redireciona para a URL padrão configurada em `get_success_url`
        return super().form_valid(form)


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

        # Verifica se o botão "Salvar e Continuar" foi pressionado
        if "save_and_continue" in self.request.POST:
            # Recarrega a mesma página com os dados preenchidos no formulário
            return self.render_to_response(self.get_context_data(form=form))

        # Caso contrário, redireciona para a URL padrão
        return super().form_valid(form)


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

