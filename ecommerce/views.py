from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from carrinho.models import Carrinho
from pedidos.models import Pedido
from pagamentos.models import Pagamento
from cupons.models import Cupom
from avaliacoes.models import Avaliacao

def index(request):
    return render(request, 'ecommerce/index.html')

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'ecommerce/produtos.html', {'produtos': produtos})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'ecommerce/produto_detail.html', {'produto': produto})

def carrinho(request):
    carrinho = Carrinho.objects.all()
    return render(request, 'ecommerce/carrinho.html', {'carrinho': carrinho})

def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'ecommerce/pedidos.html', {'pedidos': pedidos})

def pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'ecommerce/pagamentos.html', {'pagamentos': pagamentos})

def cupons(request):
    cupons = Cupom.objects.all()
    return render(request, 'ecommerce/cupons.html', {'cupons': cupons})

def avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'ecommerce/avaliacoes.html', {'avaliacoes': avaliacoes})