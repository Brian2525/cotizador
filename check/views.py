from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic  import DetailView, ListView, TemplateView
from django.views import View
from .models import Check, Categoria
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, CheckForm
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
from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class Check_control(LoginRequiredMixin): 
    @login_required
    def create_check(request):
        if request.user.is_authenticated:
            if request.method=='POST': 
                form=CheckForm(data=request.POST)
                if form.is_valid():
                    form.instance.autor = request.user
                    form.save()
                    return redirect('index') 
            else:
                form=CheckForm()
            return render(request, 'check/create.html', {'form': form })
        else: 
            return redirect('/accounts/login/')
    
   
    def read_check(request, id):
        check=get_object_or_404(Check, id=id,  autor_id=request.user )
        return render(request, 'check/view.html', {'check': check } )
    
    
    def update_check(request, id):
        check=get_object_or_404(Check, id=id, autor_id=request.user)
        if request.method=='POST': 
            form=CheckForm(data=request.POST, instance=check)
            if form.is_valid():
                form.instance.autor = request.user
                form.save()
            return redirect('check/index') #Después debe redirigir a la lista de checks creados 
        else:
            print('No es valido')
        form=CheckForm(instance=check) 
        return render(request, 'check/edit.html', {'form': form })
    
    @login_required
    def delete(request, id):
        check=get_object_or_404(Check, id=id, autor_id=request.user)
        check.delete()
        return redirect('index')




class list_check(LoginRequiredMixin,ListView):
    model=Check
   


def index(request): 
    if request.user.is_authenticated:
    #check=Check.objects.all()
        check=Check.objects.filter(autor_id=request.user)
        for obj in check:
             obj.verificar_expiracion()
             obj.save
        return render (request, 'check/index.html', {'check': check})
    else: 
         return redirect('/accounts/login/')



def renovaciones(request, id ):
    check=Check.objects.filter(id=id)
    if request.method=='POST':
        for obj in check: 
             obj.renovar_expiracion()
             print('exitoso')
        return render (request, 'check/renew.html', {'check': check})
    else: 
        return render (request, 'check/renew.html', {'check': check})

    
     
def renovar(request, id):
    check=Check.objects.filter(vigente=False, id=id)
    if request.method=='POST':
        for obj in check: 
             obj.renovar_expiracion()
             obj.save
        return render (request, 'check/renew.html', {'check': check})
    else: 
         return redirect('check/index')
     
     


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
            template = get_template('check/pdf.html')
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
        return HttpResponseRedirect(reverse_lazy('check/index'))
        
"""

class PdfView(View):
    
    def get(self,request, *args, **kwargs):
        try:
    # Datos para pasar al template
            context= {'check': Check.objects.get(pk=self.kwargs['pk']), 
                            #'logo': '{}{}'.format(settings.STATIC_URL, 'img/correo.png') , 
                            #'logo2': (settings.STATIC_URL+ 'check/img/logo.png') , 
                           'logo3': '{}{}'.format(settings.STATIC_URL,'check/img/logo.png') ,
                            'otro': 'otra cosa'}
            print(context)
           
    
            # Renderizamos el template a HTML
            html_string = render_to_string('invoice.html', context)
            
            # Convertimos el HTML a PDF usando WeasyPrint
            html = HTML(string=html_string)
            #css_url=CSS(string=)
           
            pdf = html.write_pdf()

            # Generamos la respuesta HTTP con el PDF
            response = HttpResponse(pdf, content_type='application/pdf')
            #response = HttpResponse(html_string)
            response['Content-Disposition'] = 'inline; filename="reporte.pdf"'
        except:
            pass

        return response




"""
"""
    def get(self,request, *args, **kwargs): 
        try:  
            #Datos para pasar al pdf
            context= {'check': Check.objects.get(pk=self.kwargs['pk']), 
                    'logo': '{}{}'.format(settings.STATIC_URL, 'img/correo.png') , 
                    'logo2': '{}{}'.format(settings.STATIC_URL, 'img/logo.png') , 
                    'otro': 'otra cosa'}
            template = get_template('page_detail.html')
            html= template.render(context)
            #css_url=os.path.join(settings.BASE_DIR, '/static/lib/css/bootstrap.min.css') 
            #print(css_url)
            pdf=HTML(string=html).write_pdf(stylesheets=[CSS()])
            return HttpResponse (pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('index'))
"""