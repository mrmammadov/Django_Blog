from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from  .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'posts'

@login_required
def about(request):
    # if not request.user.is_authorized:
    return render(request, 'blogs/about.html')