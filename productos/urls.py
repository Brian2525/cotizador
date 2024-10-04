from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.item_list, name='producto_list'),
    path('producto/create/', views.item_create, name='producto_create'),
    path('producto/update/<int:pk>/', views.item_update, name='producto_update'),
    path('producto/delete/<int:pk>/', views.item_delete, name='producto_delete'),
]
