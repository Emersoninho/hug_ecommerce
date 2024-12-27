from django.shortcuts import render, redirect
from.models import Pagamento

def pagamentos(request):
    pagamentos = Pagamento.objects.filter(usuario=request.user)
    return render(request, 'pagamentos/pagamentos.html', {'pagamentos': pagamentos})

def pagamento_pix(request):
    # Implementar lógica para pagamento com Pix
    return redirect('pagamentos:pagamentos')

def pagamento_boleto(request):
    # Implementar lógica para pagamento com Boleto
    return redirect('pagamentos:pagamentos')

def pagamento_cartao(request):
    # Implementar lógica para pagamento com Cartão
    return redirect('pagamentos:pagamentos')