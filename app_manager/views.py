from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app_associados.models import AssociadoModel, ReparticaoModel, MunicipiosCircusnscricaoModel
from django.db.models import Count

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'app_manager/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_associados'] = AssociadoModel.objects.count()
        context['associados_ativos'] = AssociadoModel.objects.filter(status="Ativo(a)").count()
        context['associados_aposentados'] = AssociadoModel.objects.filter(status="Aposentado(a)").count()
        context['associados_homens'] = AssociadoModel.objects.filter(sexo_biologico="Masculino").count()
        context['associados_mulheres'] = AssociadoModel.objects.filter(sexo_biologico="Feminino").count()
        context['associados_indefinidos'] = AssociadoModel.objects.filter(sexo_biologico="").count()


        # Contagem de associados por repartição
        associados_por_reparticao = (
            AssociadoModel.objects
            .values('reparticao__nome_reparticao')  # Pega o nome da repartição associada
            .annotate(associados_count=Count('id'))  # Conta os associados em cada repartição
            .order_by('reparticao__nome_reparticao')
        )

        # Contagem de associados por município de circunscrição
        associados_por_municipio_circunscricao = (
            AssociadoModel.objects
            .values('municipio_circunscricao__municipio')  # Pega o nome do município de circunscrição
            .annotate(associados_count=Count('id'))  # Conta os associados em cada município
            .order_by('municipio_circunscricao__municipio')
        )

        context['associados_por_reparticao'] = associados_por_reparticao
        context['associados_por_municipio_circunscricao'] = associados_por_municipio_circunscricao
        return context
