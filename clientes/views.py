from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.views.generic  import DetailView, ListView, TemplateView



# Create your views here.


class list_cliente(ListView):
    model=Cliente



class detail_cliente(DetailView):
    model=Cliente





def create_cliente(request):
    if request.user.is_authenticated:
        if request.method=='POST': 
            form=ClienteForm(data=request.POST)
            if form.is_valid():
                form.instance.autor = request.user
                form.save()
                return redirect('clientes') 
        else:
            form=ClienteForm()
        return render(request, 'clientes/create.html', {'form': form })
    else: 
        return redirect('/accounts/login/')
    
   
def read_check(request, id):
    check=get_object_or_404(Cliente, id=id,  autor_id=request.user )
    return render(request, 'clientes/view.html', {'check': check } )
    
    
def update_check(request, id):
    check=get_object_or_404(Cliente, id=id)
    if request.method=='POST': 
        form=ClienteForm(data=request.POST, instance=check)
        if form.is_valid():

            form.save()
        return redirect('clientes') #Después debe redirigir a la lista de checks creados 
    else:
        print('No es valido')
    form=ClienteForm(instance=check) 
    return render(request, 'clientes/edit.html', {'form': form })
    
    
def delete(request, id):
    check=get_object_or_404(Cliente, id=id)
    check.delete()
    return redirect('clientes')

   