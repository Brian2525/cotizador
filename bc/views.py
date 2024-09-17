from typing import Any
from django.shortcuts import render, redirect, get_object_or_404 
from .forms import VendedoresForm, Vendedores
from .models import Vendedores
from cotizaciones.models import Check
from .forms import VendedoresForm
from clientes.forms import ClienteForm
from django.db.models import Sum
from django.views.generic  import DetailView, ListView, TemplateView





class listar_vendedores(ListView):
    model=Vendedores



class vendedor(DetailView):
    model=Vendedores
    template_name='vendedores_detail.html'
  

# Create  vendedor
def Cvendedor(request):
    if request.method=='POST': 
        form=VendedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedores') 
    else:
        form=VendedoresForm()
    return render(request, 'bc/create.html', {'form': form })
    


def update_vendedor(request, id):
    check=get_object_or_404(Vendedores, id=id)
    if request.method=='POST': 
        form=VendedoresForm(data=request.POST, instance=check)
        if form.is_valid():
            form.save()
        return redirect('vendedores') #Después debe redirigir a la lista de checks creados 
    else:
        print('No es valido')
    form=VendedoresForm(instance=check) 
    return render(request, 'bc/edit.html', {'form': form })


def dashbord_vendedor(request,id):
   vendedor=get_object_or_404(Vendedores, id=id)
   total_checks=Check.objects.filter(autor=vendedor.id).count()
   #checks= get_object_or_404(autor=vendedor)# quiero sber cuantos checks ha generado
   #numero_checks=len(checks)
   #total_checks= checks.aaggregate(Sum('precio_objetivo'))['monto_sum']
   context = {
        'vendedor': vendedor,
        #'checks': checks,
        #'numero_checks':numero_checks,
        #'total_cotizaciones': total_checks,
    }
   return render(request, 'bc/dash_vendor.html', context)


#vista de business Card con formulario de contacto    
def bc(request, id):
    vendedor=get_object_or_404(Vendedores, id=id)
    form=ClienteForm()

    context={ 'vendedor': vendedor, 
                     'form':form} 

    if request.method=='POST': 
        form=ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')  
    else:
        form
    return render (request, 'bc/business_card.html', context )
   





def delete(request, id):
    obj=get_object_or_404(Vendedores, id=id)
    obj.delete()
    return redirect('vendedores')
