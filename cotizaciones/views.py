from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic  import DetailView, ListView, TemplateView
from django.views import View
from .models import Check, Categoria, Comentarios
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, CheckForm, ComentariosForm
from django.template.loader import get_template
from django.templatetags.static import static
from django.http import HttpResponse, request, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#weasy HTML to PDF 
import functools

from django.conf import settings
from django.views.generic import DetailView
from django.utils import timezone
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import WeasyTemplateResponse
from django_weasyprint.utils import django_url_fetcher
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from cotizador.wsgi import *
from cotizador import settings


#HTML2PDF

import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

#CRUD Usuario Gerente

class Check_control(LoginRequiredMixin): 
    @login_required
    def create_check(request):
        form=CheckForm()
        if request.user.is_authenticated:
            if request.method=='POST': 
                form=CheckForm(data=request.POST)
                if form.is_valid():
                    form.instance.autor = request.user
                    form.save()
                return redirect('cotizaciones') 
            else:
                form=CheckForm()
            return render(request, 'cotizaciones/create.html', {'form': form })
        else: 
            return redirect('/accounts/login/')
    


    def read_check(request, id):
        check=get_object_or_404(Check, id=id,  autor_id=request.user)
        comentarios=Comentarios.objects.filter(check_asociado=check.id)
        form2=ComentariosForm(data=request.POST)
        if form2.is_valid():
             form2.instance.autor_comentario = request.user
             form2.instance.check_asociado = check
             form2.save()
        context ={
                  'check':check,
                  'form2': form2,
                  'comentarios': comentarios,
        }

        return render(request, 'cotizaciones/view.html', context)
    
    

    def update_check(request, id):
        check=get_object_or_404(Check, id=id, autor_id=request.user)
        comentarios=Comentarios.objects.filter(check_asociado=check.id)
        form=CheckForm(instance=check)
        form2=ComentariosForm()
        context ={
                  'check':check,
                  'comentarios': comentarios,
                  'form':form,
                  'form2':form2, 
        }
        if request.method=='POST': 
            form=CheckForm(data=request.POST, instance=check)
            form2=ComentariosForm(data=request.POST)
            if form2.is_valid():
                form2.instance.autor_comentario = request.user
                form2.instance.check_asociado = check
                form2.save()
            if form.is_valid():
                form.instance.autor = request.user
                form.save()

             #Después debe redirigir a la lista de checks creados 
        else:
            print('No es valido')
            form=CheckForm(instance=check) 
        
        return render(request, 'cotizaciones/edit.html', context)





    @login_required
    def delete(request, id):
        check=get_object_or_404(Check, id=id, autor_id=request.user)
        check.delete()
        return redirect('cotizaciones')

#Vistas


#CRUD Usuario IDI 

class Check_idi(LoginRequiredMixin): 

    def read_check(request, id):
        check=get_object_or_404(Check, id=id)
        comentarios=Comentarios.objects.filter(check_asociado=check.id)
        form2=ComentariosForm(data=request.POST)
        if form2.is_valid():
             form2.instance.autor_comentario = request.user
             form2.instance.check_asociado = check
             form2.save()
        context ={
                  'check':check,
                  'form2': form2,
                  'comentarios': comentarios,
        }

        return render(request, 'cotizaciones/view.html', context)
    
    

    def update_check(request, id):
        check=get_object_or_404(Check, id=id)
        comentarios=Comentarios.objects.filter(check_asociado=check.id)
        form=CheckForm(instance=check)
        form2=ComentariosForm()
        context ={
                  'check':check,
                  'comentarios': comentarios,
                  'form':form,
                  'form2':form2, 
        }
        if request.method=='POST': 
            form=CheckForm(data=request.POST, instance=check)
            form2=ComentariosForm(data=request.POST)
            if form2.is_valid():
                form2.instance.autor_comentario = request.user
                form2.instance.check_asociado = check
                form2.save()
            if form.is_valid():
                form.instance.autor = request.user
                form.save()

             #Después debe redirigir a la lista de checks creados 
        else:
            print('No es valido')
            form=CheckForm(instance=check) 
        
        return render(request, 'cotizaciones/edit.html', context)
    
    def list_idi(request): 
        if request.user.is_authenticated:
            check=Check.objects.all()
            #related_check=Check.objects.filter(autor_id=request.user)
            context ={
                    'check':check,
                    #'related_check': related_check,
                    
            }
            for obj in check:
                obj.verificar_expiracion()
                obj.save
            return render (request, 'cotizaciones/list_idi.html', {'check': check})
        else: 
            return redirect('/accounts/login/')




#Para filtrar los checks por usuario
def list(request): 
    if request.user.is_authenticated:
        #check=Check.objects.all()
        check=Check.objects.filter(autor_id=request.user)
        context ={
                  'check':check,
                  #'related_check': related_check,
                   
        }
        for obj in check:
             obj.verificar_expiracion()
             obj.save
        return render (request, 'cotizaciones/list.html', {'check': check})
    else: 
         return redirect('/accounts/login/')


        




#Renovaciones
def renovaciones(request, id ):
    check=Check.objects.filter(id=id)
    if request.method=='POST':
        for obj in check: 
             obj.renovar_expiracion()
             print('exitoso')
        return render (request, 'cotizaciones/renew.html', {'check': check})
    else: 
        return render (request, 'cotizaciones/renew.html', {'check': check})

    
     
def renovar(request, id):
    check=Check.objects.filter(vigente=False, id=id)
    if request.method=='POST':
        for obj in check: 
             obj.renovar_expiracion()
             obj.save
        return render (request, 'cotizaciones/renew.html', {'check': check})
    else: 
         return redirect('cotizaciones')
     
     


def unsecure(request):   
    return render(request,"unsecure.html",{})  


def secure(request):   
    return render(request,"secure.html",{})






    






class PdfView(View): 
    
    def link_callback(uri, rel):
            
    #        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
     #       resources

            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise RuntimeError(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
   
    def get(self,request, *args, **kwargs): 
        imagen_url= '{}{}'.format(settings.MEDIA_URL, 'img/logo.png') 
        print(imagen_url)
        try:  
            template = get_template('cotizaciones/pdf.html')
            context= {'check': Check.objects.get(pk=self.kwargs['pk']),  
                    'logo2': imagen_url, 
                    'otro': 'otra cosa'}
            html= template.render(context)
            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type='application/pdf')
           #  response['Content-Disposition'] = 'attachment; filename=" descarga.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response, 
                link_callbacks=self.link_callback
                )
            # if error then show some funny view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        except: 
            pass
        return HttpResponseRedirect(reverse_lazy('cotizaciones'))