from django.shortcuts import render, redirect, get_object_or_404
from.models import Pedido
from carrinho.models import Carrinho

def pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'pedidos/pedidos.html', {'pedidos': pedidos})

def criar_pedido(request):
    carrinho = Carrinho.objects.filter(usuario=request.user)
    pedido = Pedido.objects.create(usuario=request.user)
    for item in carrinho:
        pedido.itens.add(item)
    carrinho.delete()
    return redirect('pedidos:pedidos')

def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedidos/pedido_detail.html', {'pedido': pedido})