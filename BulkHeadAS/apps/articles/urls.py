from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('myaccount/', views.MyAccountView.as_view(), name='myaccount'),
    path('services/', views.ShowServices.as_view(), name = 'service')
    ]