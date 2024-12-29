from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.carrinho, name='criar_pedido'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('limpar/', views.limpar_carrinho, name='limpar_carrinho')
]
