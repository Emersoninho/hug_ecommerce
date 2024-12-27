from django.urls import path
from. import views

urlpatterns = [
    path('', views.avaliacoes, name='avaliacoes'),
    path('<int:pk>/', views.avaliacao_detail, name='avaliacao_detail'),
    path('criar/', views.criar_avaliacao, name='criar_avaliacao'),
]