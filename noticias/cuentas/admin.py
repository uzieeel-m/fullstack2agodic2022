from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FormularioCreacionUsuarioPersonalizado, FormularioCambioUsuarioPersonalizado
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form = FormularioCreacionUsuarioPersonalizado
    form = FormularioCambioUsuarioPersonalizado
    model = UsuarioPersonalizado
    list_display = ['email', 'username', 'edad', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('edad',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('edad')}),
    )

# Register your models here.
admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)