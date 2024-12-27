from django.shortcuts import render, get_object_or_404
from.models import Produto

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/produto_detail.html', {'produto': produto})

def produtos_por_categoria(request, categoria):
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'produtos/produtos_por_categoria.html', {'produtos': produtos})