from django.contrib import messages
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .models import Client
from django.views.generic import ListView
from . models import Services
from .forms import Entrollment

class MyAccountView(CreateView):
    model = Client
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
        if form.is_valid():
            messages.success(request, 'Пришла новая заявка!')
            form.save()
            return redirect('index')
        else:
            messages.error(request, 'Пользователь пытается оставить заявку')
    return render(request, 'entrollment.html', {'form': Entrollment})