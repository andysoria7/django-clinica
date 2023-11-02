from django.shortcuts import render
from .forms import FormCorreo
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from usuarios.models import UsuarioPersonalizado
from functools import wraps # Es un decorador que nos va a permitir preservar la informacion de la funcion original.
from django.shortcuts import redirect


# Create your views here.

def solo_miembros_del_personal(vista_protegida):
    @wraps(vista_protegida) # Usamos el decorador wraps para preservar la informacion de la funcion original.
    def _vista_envuelta(request, *args, **kwargs): # Estoy definiendo una funcion interna que envuelve la funcion original.
        if not request.user.is_authenticated:
            return redirect('login')
        elif not request.user.is_staff:
            return redirect('/')
        else:
            return vista_protegida(request, *args, **kwargs)
    return _vista_envuelta
    

@solo_miembros_del_personal
@csrf_protect
def enviar_correo(request):
    mensaje_error = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        if not nombre:
            return JsonResponse({'success': False, 'errores': {'nombre': ['Por favor, completa tu nombre en el perfil']}})
        if not request.user.email:
            mensaje_error = {'email': ['No cuentas con email. Completa el campo en el perfil']}
            return JsonResponse({'success': False, 'errores': mensaje_error})
            
        form = FormCorreo(request.POST)
            
        if form.is_valid():
            asunto = form.cleaned_data['asunto']  # Asegúrate de que el nombre de campo coincida con tu formulario.
            mensaje = form.cleaned_data['mensaje']  # Asegúrate de que el nombre de campo coincida con tu formulario.
            
            # Para enviar con mailtrap.
            send_mail(asunto, mensaje, 'andycorreo@gmail.com', ['correo_destino@mailtrap.io'], fail_silently=False)
            form.save()
            
            return JsonResponse({"success": True})
        else:
            errores = form.errors.as_data()
            mensaje_error = {}
            for campo, lista_errores in errores.items():
                if campo == '__all__': # Para eliminar la palabra __all__ del metodo clean.
                    campo = form.campos_validados
                errores_str = []
                for error in lista_errores:
                    errores_str.append(str(error))
                mensaje_error[(str(campo))] = errores_str
            return JsonResponse({'success': False, 'errores': mensaje_error})
            
    else:
        if request.user.is_authenticated:
            if request.user.first_name and request.user.last_name:
                nombre_inicial = request.user.first_name
                apellidos_iniciales = request.user.last_name
            else:
                nombre_inicial = request.user.first_name
                apellidos_iniciales = None
            
        else:
            nombre_inicial = None
            apellidos_iniciales = None
            
        # En caso cuya solicitud no sea POST
        form = FormCorreo(nombre_inicial=nombre_inicial, apellidos_iniciales = apellidos_iniciales, usuario_actual=request.user)
        return render(request,'enviar.html', {'form':form})
@solo_miembros_del_personal
def correo(request):
    return render(request,'correo.html')



        
