from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import SocialPost
from django.urls import reverse_lazy

class SocialPostListView(LoginRequiredMixin, ListView):
    model = SocialPost
    template_name = 'socialpost_list.html'

class SocialPostDetailView(LoginRequiredMixin, DetailView):
    model = SocialPost
    template_name = 'socialpost_detail.html'

class SocialPostUpdateView(LoginRequiredMixin, UpdateView):
    model = SocialPost
    fields = ('title', 'body',)
    template_name = 'socialpost_edit.html'

class SocialPostDeleteView(LoginRequiredMixin, DeleteView):
    model = SocialPost
    template_name = 'socialpost_delete.html'
    success_url = reverse_lazy('socialpost_list')

class SocialPostCreateView(LoginRequiredMixin, CreateView):
    model = SocialPost
    template_name = 'socialpost_create.html'
    fields = ('title', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

