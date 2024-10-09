from django.urls import path
from . import views


urlpatterns = [
 path('empresas/', views.empresa_list, name='empresa_list'),
    path('empresas/create/', views.empresa_create, name='empresa_create'),
    path('empresas/<int:pk>/update/', views.empresa_update, name='empresa_update'),
    path('empresas/<int:pk>/delete/', views.empresa_delete, name='empresa_delete'),

    ]

