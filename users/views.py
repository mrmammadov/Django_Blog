from django.shortcuts import render, HttpResponse
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            return HttpResponse(form.cleaned_data.get('your_name'))
    
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
