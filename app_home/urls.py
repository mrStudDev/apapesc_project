
from django.urls import path
from . views import HomeListView, ApapescListView

app_name = 'app_home'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('apapesc/', ApapescListView.as_view(), name='lista_apapesc'),

]