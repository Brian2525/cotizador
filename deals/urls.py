# deals/urls.py

from django.urls import path
from .views import (
    DealListView,
    DealDetailView,
    DealCreateView,
    DealUpdateView,
    DealDeleteView,
)

urlpatterns = [
    path('deals/', DealListView.as_view(), name='deal_list'),
    path('deals/<int:pk>/', DealDetailView.as_view(), name='deal_detail'),
    path('deals/create/', DealCreateView.as_view(), name='deal_create'),
    path('deals/<int:pk>/update/', DealUpdateView.as_view(), name='deal_update'),
    path('deals/<int:pk>/delete/', DealDeleteView.as_view(), name='deal_delete'),
]
