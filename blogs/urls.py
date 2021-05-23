from django.urls import path
from . import views
from blogs.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blogs-home'),
    path('posts/new/', PostCreateView.as_view(), name='blogs-create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='blogs-detail'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='blogs-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='blogs-delete'),
    path('about/', views.about, name='blogs-about'),
]