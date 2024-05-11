
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    rut = models.CharField(max_length=20, unique=True, help_text="Ingrese el RUT sin puntos ni guión")

    def validate_unique(self, exclude=None):
        exclude = ('rut',) if exclude is None else tuple(exclude) + ('rut',)
        super().validate_unique(exclude=exclude)