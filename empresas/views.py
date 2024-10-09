from django.shortcuts import render, get_object_or_404, redirect
from empresas.models import Empresa
from empresas.forms import EmpresaForm

# Create your views here.


# Empresa CRUD
def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/empresa_list.html', {'empresas': empresas})



def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')
    else:
        form = EmpresaForm()
    return render(request, 'empresas/empresa_form.html', {'form': form})



def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresas/empresa_form.html', {'form': form})



def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa_list')
    return render(request, 'empresas/empresa_confirm_delete.html', {'empresa': empresa})

