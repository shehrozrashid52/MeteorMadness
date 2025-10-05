from django.urls import path
from . import views

app_name = 'visualizer'

urlpatterns = [
    path('', views.visualizer, name='visualizer'),
    path('orbit/<str:asteroid_id>/', views.orbit_view, name='orbit_view'),
]