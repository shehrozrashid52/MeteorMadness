from django.urls import path
from . import views

app_name = 'simulation'

urlpatterns = [
    path('', views.simulation, name='simulation'),
    path('calculate/', views.calculate_impact, name='calculate_impact'),
]