from django.urls import path
from . import views

urlpatterns = [
    # Empresa URLs
    path('empresas/', views.empresa_list, name='empresa_list'),
    path('empresas/create/', views.empresa_create, name='empresa_create'),
    path('empresas/<int:pk>/update/', views.empresa_update, name='empresa_update'),
    path('empresas/<int:pk>/delete/', views.empresa_delete, name='empresa_delete'),

    # Cliente URLs
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/create/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/update/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]