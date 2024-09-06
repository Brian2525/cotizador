from django.shortcuts import render, redirect, get_object_or_404 
from .forms import VendedoresForm, Vendedores
from .models import Vendedores
from django.views.generic  import DetailView, ListView, TemplateView





class listar_vendedores(ListView):
    model=Vendedores


class bc(DetailView):
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
    
    

    
def delete(request, id):
    obj=get_object_or_404(Vendedores, id=id)
    obj.delete()
    return redirect('vendedores')
