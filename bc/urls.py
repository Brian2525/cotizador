from django.urls import path
from . import views



urlpatterns=[
    path('vendedores',views.listar_vendedores.as_view(), name='vendedores'),
    path('vendorAdmin/<int:id>',views.dashbord_vendedor, name='vendorAdmin'),
    path('vendedor/<int:pk>',views.vendedor.as_view(), name='vendedor'),
    path('eVendedor/<int:id>',views.update_vendedor, name='vendedorU'),
    path('Cvendedor',views.Cvendedor, name='vendedorC'),
    path('eliminarVendedor/<int:id>',views.delete, name='vendedorD'),
    path('bc/<int:id>',views.bc, name='bc'),

]