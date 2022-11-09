#./cuentas/forms.py
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPersonalizado

class FormularioCreacionUsuarioPersonalizado(UserCreationForm):

    #subclase que sirve para sobreescribir los campos
    class Meta(UserCreationForm):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ('edad',)

class FormularioCambioUsuarioPersonalizado(UserChangeForm):

    class Meta:
        model = UsuarioPersonalizado
        fields = UserChangeForm.Meta.fields