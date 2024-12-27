from django.urls import path
from. import views

urlpatterns = [
    path('', views.cupons, name='cupons'),
    path('criar/', views.criar_cupom, name='criar_cupom'),
    path('<int:pk>/', views.cupom_detail, name='cupom_detail'),
]