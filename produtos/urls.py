from django.urls import path
from . import views

urlpatterns = [
    path('pesquisa_produto/', views.pesquisa_produto, name="pesquisa_produto"),
    # path('escoher_produto/', views.escolher_produto, name="escolher_produto"),
    # path('visualizar_produto', views.visualizar_produto, name="visualizar_produto")
]