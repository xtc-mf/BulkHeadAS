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
    allServices = Services.objects.all()
    sorted_services_name = sorted(allServices, key=lambda service: service.service_name)
    context= {'allServices': allServices,
              'sorted_services_name': sorted_services_name,
              }
    template_name = 'services.html'

def index(request):
    return render(request, 'main.html')
def about(request):
    return render(request, 'about/about.html')

def serviceEntrollment(request):
    if request.method == "POST":
        form = Entrollment(request.POST)
        if form.is_valid():
            messages.success(request, 'Заявка успешно оставлена!')
            form.save()
        else:
            messages.error(request, 'Ошибка заполнения формы!')
    return render(request, 'entrollment.html', {'form': Entrollment})