from django.urls import path, include
from . import views
from django.conf.urls import handler404


urlpatterns=[
    
    path('',views.list, name='cotizaciones'),
    path('idi/', views.Check_idi.list_idi , name='idi'),
    path('idi/ver/<int:id>/', views.Check_idi.read_check, name='verIdi'),
    path('idi/editar/<int:id>', views.Check_control.update_check, name='editarIdi'),
    path('create', views.Check_control.create_check , name='create'),
    path('editar/<int:id>', views.Check_control.update_check, name='editar'),
    path('ver/<int:id>/', views.Check_control.read_check, name='ver'),
    path('delete/<int:id>/', views.Check_control.delete, name='delete'),
    path('pdf/<int:pk>/', views.PdfView.as_view(), name='pdf'),
    path('renovaciones/<int:id>', views.renovaciones, name='renovar'),
    path('accounts/', include('django.contrib.auth.urls')),
   

]

