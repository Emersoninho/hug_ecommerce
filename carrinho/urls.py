from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho, name='carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('limpar/', views.limpar_carrinho, name='limpar_carrinho')
]
