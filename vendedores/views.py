from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Vendedor
from .forms import VendedorForm

# Listar vendedores
def vendedor_list(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedores/vendedor_list.html', {'vendedores': vendedores})

# Crear un nuevo vendedor
def vendedor_create(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = VendedorForm()
    return render(request, 'vendedores/vendedor_form.html', {'form': form})

# Editar un vendedor
def vendedor_update(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = VendedorForm(instance=vendedor)
    return render(request, 'vendedores/vendedor_form.html', {'form': form})

# Eliminar un vendedor
def vendedor_delete(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        vendedor.delete()
        return redirect('vendedor_list')
    return render(request, 'vendedores/vendedor_confirm_delete.html', {'vendedor': vendedor})
# Create your views here.
