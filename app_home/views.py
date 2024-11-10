from django.views.generic import ListView
from .models import Home

class HomeListView(ListView):
    model = Home
    template_name = 'app_home/home.html'
    context_object_name = 'homes'

