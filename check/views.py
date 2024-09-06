from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Check, Categoria
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, CheckForm
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.


def index(request): 
    objects=Check.objects.all()
    return render (request, 'index.html',{'objects': objects})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Cambia 'home' por la URL de tu página de inicio
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form })

def create_check(request):
    if request.method=='POST': 
        form=CheckForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') #Después debe redirigir a la lista de checks creados 
    else:
        form=CheckForm()
    return render(request, 'check_form.html', {'form': form })


def edit_check(request, id):
    check=get_object_or_404(Check, id=id)
    if request.method=='POST': 
        form=CheckForm(data=request.POST, instance=check)
        if form.is_valid():
            form.save()
            return redirect('index') #Después debe redirigir a la lista de checks creados 
    else:
        form=CheckForm(instance=check)
    return render(request, 'edit.html', {'form': form })

def ver_check(request, id):
    check=get_object_or_404(Check, id=id)
    return render(request, 'page_detail.html', {'check': check })

def pdf_check(request, id): 
    check=get_object_or_404(Check, id=id)
    template=get_template('page_detail.html')
    html=template.render({'check':check})

    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']=f'filename="check_{check.numero_cotizacion}"'

    HTML(string=html).write_pdf(response)

    return response



   