from django.shortcuts import render, redirect, get_object_or_404
from.models import Carrinho
from produtos.models import Produto

def carrinho(request):
    carrinho = Carrinho.objects.filter(usuario=request.user)
    return render(request, 'carrinho/carrinho.html', {'carrinho': carrinho})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user, produto=produto)
    if not created:
        carrinho.quantidade += 1
        carrinho.save()
    return redirect('carrinho:carrinho')

def remover_do_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho = Carrinho.objects.filter(usuario=request.user, produto=produto)
    if carrinho.exists():
        carrinho.delete()
    return redirect('carrinho:carrinho')

def limpar_carrinho(request):
    carrinho = Carrinho.objects.filter(usuario=request.user)
    carrinho.delete()
    return redirect('carrinho:carrinho')