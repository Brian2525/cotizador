from django.urls import path
from . import views



urlpatterns=[
    path('vendedores',views.listar_vendedores.as_view(), name='vendedores'),
    path('bc/<int:pk>',views.bc.as_view(), name='bc'),
    path('EVendedor/<int:pk>',views.bc.as_view(), name='vendedorU'),
    path('Cvendedor',views.Cvendedor, name='vendedorC'),
    path('eliminarVendedor/<int:id>',views.delete, name='vendedorD'),



]