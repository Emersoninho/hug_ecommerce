from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('<int:pk>/', views.produto_detail, name='produto_detail'),
    path('categoria/<str:categoria>/', views.produtos_por_categoria, name='produtos_por_categoria'),
]