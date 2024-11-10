
from django.urls import path
from . views import HomeListView

app_name = 'app_home'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),

]