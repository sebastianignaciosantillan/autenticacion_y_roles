from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('administrador', 'Administrador'),
        ('supervisor', 'Supervisor'),
        ('empleado', 'Empleado'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def is_administrador(self):
        return self.role == 'administrador'

    def is_supervisor(self):
        return self.role == 'supervisor'
    
    def is_empleado(self):
        return self.role == 'empleado'
