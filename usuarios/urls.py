from django.contrib.auth import views as auth_view
from django.urls import path
from .forms import MiFormularioDeAutenticacion
from .views import mi_vista_inicio_sesion, mi_vista_cierre_sesion

urlpatterns = [
    path('login/', mi_vista_inicio_sesion, {'form_class':MiFormularioDeAutenticacion}, name='login'), # Pasamos el dicionario form_class y le damos contexto con nuestra clase que hicimos en forms.py.
    path('logout/', mi_vista_cierre_sesion, {'next_page': '/registro/login'}, name='logout'), # Le pasamos el diccionario next_page y el contexto para que redireccione a nuestro login.
]
