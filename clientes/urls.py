from django.urls import path
from . import views

urlpatterns=[


 path('clientes',views.list_cliente.as_view(), name='clientes'),
 path('clienteNuevo',views.create_cliente, name='clienteN'),
 path('clienteVista/<pk>',views.detail_cliente.as_view(), name='clienteV'),
 path('editarCliente/<int:id>',views.update_check, name='clienteU'),
 path('eliminarCliente/<int:id>',views.delete, name='clienteD'),

]
