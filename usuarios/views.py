from django.contrib.auth import views as auth_views
from django.shortcuts import render ,redirect

# Create your views here.

def mi_vista_inicio_sesion(request, *args, **kwargs):
    form_class = kwargs.get('form_class')
    if request.user.is_authenticated:
        return redirect('/')
    return auth_views.LoginView.as_view(form_class=form_class)(request, *args, **kwargs)

def mi_vista_cierre_sesion(request, *args, **kwargs):
    next_page = kwargs.get('next_page') # Sirve para que pueda redireccionar a nuestra pagina de login y no al administrador de django.
    if not request.user.is_authenticated:
        return redirect('login')
    return auth_views.LogoutView.as_view(next_page=next_page)(request, *args, **kwargs)