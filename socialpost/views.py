from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import SocialPost
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from django.views import View

class SocialPostListView(LoginRequiredMixin, ListView):
    model = SocialPost
    template_name = 'socialpost_list.html'

class CommentGet(DetailView):
    model = SocialPost
    template_name = 'socialpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = SocialPost
    form_class = CommentForm
    template_name='socialpost_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        comment = form.save(commit=False)
        comment.socialpost = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        socialpost = self.get_object()
        return reverse('socialpost_detail', kwargs={'pk': socialpost.pk})

class SocialPostDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class SocialPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SocialPost
    fields = ('title', 'body',)
    template_name = 'socialpost_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class SocialPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SocialPost
    template_name = 'socialpost_delete.html'
    success_url = reverse_lazy('socialpost_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class SocialPostCreateView(LoginRequiredMixin, CreateView):
    model = SocialPost
    template_name = 'socialpost_create.html'
    fields = ('title', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)