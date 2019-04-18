from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('blog-posts/', PostListView.as_view(), name='blog-posts'),
    path('blog-posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog-posts/new/', PostCreateView.as_view(), name='post-create'),
    path('blog-posts/<int:pk>/update/',
         PostUpdateView.as_view(), name='post-update'),
    path('blog-posts/<int:pk>/delete/',
         PostDeleteView.as_view(), name='post-delete'),
    path('services/', views.services, name='blog-services'),
]
