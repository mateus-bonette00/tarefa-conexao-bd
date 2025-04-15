from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pedido/', views.index, name='index'),
    path('relatorio/', views.relatorio_pedido, name='relatorio_pedido'),
    path('ranking/', views.ranking_funcionarios, name='ranking_funcionarios'), 
    path('injection/', views.sql_injection_teste, name='sql_injection_teste'), 
]