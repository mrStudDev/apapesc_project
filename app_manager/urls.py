# Views Manager
from django.urls import path
from .views import DashboardView

app_name = 'app_manager'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # Outras URLs...
]