from django.urls import path
from. import views

urlpatterns = [
    path('', views.pagamentos, name='pagamentos'),
    path('pix/', views.pagamento_pix, name='pagamento_pix'),
    path('boleto/', views.pagamento_boleto, name='pagamento_boleto'),
    path('cartao/', views.pagamento_cartao, name='pagamento_cartao'),
]