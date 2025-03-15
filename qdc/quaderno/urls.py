"""
URL configuration for qdc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import lista_campi, lista_mezzi, lista_operatore, home, lista_attivita, cambia_status_attivita, lista_trattamenti, modifica_attivita, modifica_trattamento, menu
#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('campi/', lista_campi, name='lista_campi'),
    path('mezzi/', lista_mezzi, name='lista_mezzi'),
    path('operatore/', lista_operatore, name='lista_operatore'),
    path('attivita/', lista_attivita, name='lista_attivita'),
    path('attivita/<int:attivita_id>/modifica/', modifica_attivita, name='modifica_attivita'),
    path('attivita_semplice/<int:attivita_id>/cambia_status/', cambia_status_attivita, name='cambia_status_attivita'),
    path('trattamenti/', lista_trattamenti, name='lista_trattamenti'),
    path('trattamenti/<int:trattamento_id>/modifica/', modifica_trattamento, name='modifica_trattamento'),
    ##path('accounts/login/', auth_views.LoginView.as_view()),
    path('admin/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]

