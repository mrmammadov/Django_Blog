from django.urls import path
from . import views
from blogs.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blogs-home'),
    path('about/', views.about, name='blogs-about'),
]