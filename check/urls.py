from django.urls import path 
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('login',views.login_view, name='login'),
    path('create', views.create_check, name='create'),
    path('editar/<int:id>', views.edit_check, name='editar'),
    path('ver/<int:id>/', views.ver_check, name='ver'),
    path('ver/<int:id>/', views.pdf_check, name='pdf')

]