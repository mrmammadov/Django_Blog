from django.shortcuts import render
from django.http import HttpResponse
from  .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    print(context['posts'][0].date_posted)
    return render(request, 'blogs/home.html', context)

def about(request):
    return HttpResponse('<h1>About Page</h1>')