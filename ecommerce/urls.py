from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('produto/<int:pk>/', views.produto_detail, name='produto_detail'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pagamentos/', views.pagamentos, name='pagamentos'),
    path('cupons/', views.cupons, name='cupons'),
    path('avaliacoes', views.avaliacoes, name='avaliacoes'),
]
