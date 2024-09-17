from django.shortcuts import render, redirect, get_object_or_404
from cotizaciones.models import Check
from clientes.models import Cliente
from bc.models import Vendedores

# Create your views here.
def index(request):
    total_checks=Check.objects.count()
    total_clientes=Cliente.objects.count()
    total_vendedores=Vendedores.objects.count()
    


    context ={
        'total_checks':total_checks,
        'total_clientes':total_clientes,
        'total_vendedores':total_vendedores
    }


    return render(request, 'dashboard/index.html', context)



