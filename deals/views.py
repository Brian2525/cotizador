# deals/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Deal
from .forms import DealForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class DealListView( ListView):
    model = Deal
    template_name = 'deals/deal_list.html'
    context_object_name = 'deals'

    def get_queryset(self):
        return Deal.objects.filter(owner=self.request.user)

class DealDetailView( DetailView):
    model = Deal
    template_name = 'deals/deal_detail.html'
    context_object_name = 'deal'

    def test_func(self):
        deal = self.get_object()
        return self.request.user == deal.owner

class DealCreateView( CreateView):
    model = Deal
    form_class = DealForm
    template_name = 'deals/deal_form.html'
    success_url = reverse_lazy('deal_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class DealUpdateView( UpdateView):
    model = Deal
    form_class = DealForm
    template_name = 'deals/deal_form.html'
    success_url = reverse_lazy('deal_list')

    def test_func(self):
        deal = self.get_object()
        return self.request.user == deal.owner

class DealDeleteView( DeleteView):
    model = Deal
    template_name = 'deals/deal_confirm_delete.html'
    success_url = reverse_lazy('deal_list')

    def test_func(self):
        deal = self.get_object()
        return self.request.user == deal.owner
