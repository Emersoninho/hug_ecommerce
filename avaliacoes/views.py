from django.shortcuts import render, redirect, get_object_or_404
from.models import Avaliacao

def avaliacoes(request):
    avaliacoes = Avaliacao.objects.filter(usuario=request.user)
    return render(request, 'avaliacoes/avaliacoes.html', {'avaliacoes': avaliacoes})

def criar_avaliacao(request):
    avaliacao = Avaliacao.objects.create(usuario=request.user)
    return redirect('avaliacoes:avaliacoes')

def avaliacao_detail(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    return render(request, 'avaliacoes/avaliacao_detail.html', {'avaliacao': avaliacao})