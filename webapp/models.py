from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profesor(models.Model):
    nombre = models.CharField(max_length=25, null=False, verbose_name=_('Nombre Profesor'), unique=True)
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)


class Grupo(models.Model):
    nombre = models.CharField(max_length=25, null=False, verbose_name=_('Nombre Grupo'), unique=True)
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)


class Horario(models.Model):
    hora_inicio = models.TimeField(verbose_name=_('Hora Inicio'))
    hora_fin = models.TimeField(verbose_name=_('Hora Fin'))
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
