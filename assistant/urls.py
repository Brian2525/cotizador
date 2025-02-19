from django.urls import path
from . import views

urlpatterns = [
    # Cliente URLs
    path('chatbot/', views.chatbot, name='chatbot'),
]
