from django.urls import path
from . import views

urlpatterns = [
    path('bc/<int:id>', views.vendedor_bc, name='bc'),
    path('vendedores/', views.vendedor_list, name='vendedor_list'),
    path('vendedores/nuevo/', views.vendedor_create, name='vendedor_create'),
    path('vendedores/<int:pk>/editar/', views.vendedor_update, name='vendedor_update'),
    path('vendedores/<int:pk>/eliminar/', views.vendedor_delete, name='vendedor_delete'),
]