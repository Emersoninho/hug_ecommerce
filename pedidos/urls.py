from django.urls import path
from. import views

urlpatterns = [
    path('', views.pedidos, name='pedidos'),
    path('<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('criar/', views.criar_pedido, name='criar_pedido'),
]