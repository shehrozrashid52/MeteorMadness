from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('asteroids/', views.asteroids, name='asteroids'),
    path('asteroid/<str:asteroid_id>/', views.asteroid_detail, name='asteroid_detail'),
    path('education/', views.education, name='education'),
    path('quiz/', views.quiz, name='quiz'),
    path('api/neo-data/', views.neo_data_api, name='neo_data_api'),
]