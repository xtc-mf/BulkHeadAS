from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import ListView
from . models import Services
from .forms import Entrollment

class MyAccountView(CreateView):
    model = Article
    template_name = 'user/profile.html'

    fields = '__all__'

class ShowServices(ListView):
    model = Services
    template_name = 'services.html'

def index(request):
    return render(request, 'main.html')
def about(request):
    return render(request, 'about/about.html')

def serviceEntrollment(request):
    if request.method == "POST":
        form = Entrollment(request.POST)
        #if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'entrollment.html', {'form': Entrollment})

