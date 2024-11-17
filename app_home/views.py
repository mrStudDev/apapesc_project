from django.views.generic import ListView
from .models import Home, ApapescModel

# views home
class HomeListView(ListView):
    model = Home
    template_name = 'app_home/home.html'
    context_object_name = 'homes'

class ApapescListView(ListView):
    model = ApapescModel
    template_name = 'app_home/apapesc.html'
    context_object_name = 'apapesc'

    def get_queryset(self):
        return ApapescModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apapesc'] = ApapescModel.objects.all()
        return context