from django.shortcuts import render, get_object_or_404
from.models import Produto

def index(request):
    return render(request, 'ecommerce/index.html')

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'ecommerce/produtos.html', {'produtos': produtos})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'ecommerce/produto_detail.html', {'produto': produto})

def carrinho(request):
    return render(request, 'ecommerce/carrinho.html')

def pedidos(request):
    return render(request, 'ecommerce/pedidos.html')

def pagamentos(request):
    return render(request, 'ecommerce/pagamentos.html')

def cupons(request):
    return render(request, 'ecommerce/cupons.html')

def avaliacoes(request):
    return render(request, 'ecommerce/avaliacoes.html')