from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informacion adicional', {'fields': ('imagen_perfil',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informacion adicional', {'fields': ('imagen_perfil',)}),
    )

# Register your models here.
admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)
