from django.shortcuts import render, redirect, get_object_or_404
from.models import Cupom

def cupons(request):
    cupons = Cupom.objects.all()
    return render(request, 'cupons/cupons.html', {'cupons': cupons})

def criar_cupom(request):
    cupom = Cupom.objects.create()
    return redirect('cupons:cupons')

def cupom_detail(request, pk):
    cupom = get_object_or_404(Cupom, pk=pk)
    return render(request, 'cupons/cupom_detail.html', {'cupom': cupom})