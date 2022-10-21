from nntplib import ArticleInfo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import SocialPost
from django.urls import reverse_lazy

class SocialPostListView(ListView):
    model = SocialPost
    template_name = 'socialpost_list.html'

class SocialPostDetailView(DetailView):
    model = SocialPost
    template_name = 'socialpost_detail.html'

class SocialPostUpdateView(UpdateView):
    model = SocialPost
    fields = ('title', 'body',)
    template_name = 'socialpost_edit.html'

class SocialPostDeleteView(DeleteView):
    model = SocialPost
    template_name = 'socialpost_delete.html'
    success_url = reverse_lazy('socialpost_list')

class SocialPostCreateView(CreateView):
    model = SocialPost
    template_name = 'socialpost_create.html'
    fields = ('title', 'body', 'author',)

