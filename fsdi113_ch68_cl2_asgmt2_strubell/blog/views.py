from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='PUBLISHED')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostDraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='DRAFT', author=self.request.user)

class PostArchivedListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_archived_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='ARCHIVED', author=self.request.user)

class ProtectedPostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail_protected.html'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user or self.request.user.is_staff

def error_403(request, exception):
    return render(request, '403.html', status=403)

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)

def trigger_error(request):
    1 / 0 # SET FOR DELIBERATE CRASH
