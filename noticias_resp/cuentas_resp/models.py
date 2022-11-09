from django.db import models
from django.contrib.auth.models import AbstractUser

#create your models here.
class UsuarioPersonalizado(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    