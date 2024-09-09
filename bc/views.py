from django.shortcuts import render, redirect, get_object_or_404 
from .forms import VendedoresForm, Vendedores
from .models import Vendedores
from .forms import VendedoresForm
from clientes.forms import ClienteForm
from django.views.generic  import DetailView, ListView, TemplateView





class listar_vendedores(ListView):
    model=Vendedores


class vendedor(DetailView):
    model=Vendedores




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
