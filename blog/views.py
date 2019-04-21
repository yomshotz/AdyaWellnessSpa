from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context_home = {
        'carousel': True,
        'footer': True,
        'title': 'Home',
        'current_nav_home': 'current',
    }

    return render(request, 'blog/home.html', context_home)


def services(request):
    context_services = {
        'carousel': True,
        'footer': True,
        'title': 'Services',
        'current_nav_services': 'current',
    }

    return render(request, 'blog/services.html', context_services)


def under_construction(request):
    context_construction = {
        'title': 'Under Construction',
        'current_nav_construction': 'current',
    }

    return render(request, 'blog/empty_content.html', context_construction)


def blog(request):
    context_blog = {
        'posts': Post.objects.all(),
    }

    return render(request, 'blog/adya-blog.html', context_blog)


class PostListView(ListView):
    model = Post
    template_name = 'blog/adya_blog.html'  # <app>/<model>_<viewtype>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  # <app>/<model>_<viewtype>
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog-posts/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
