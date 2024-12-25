from django.urls import path
from . import views

urlpatterns = [
    # Empresa URLs

    # Cliente URLs
    path('prospects', views.create_cliente, name='prospects'),
]