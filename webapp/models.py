import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profesor(models.Model):
    nombre = models.CharField(max_length=25, null=False, verbose_name=_('Nombre Profesor'), unique=True)
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _('Profesores')

    '''
        def clean(self):
        if Profesor.objects.filter(nombre=self.nombre).exists():
            raise ValidationError(_('Ya existe un profesor con ese nombre'))
    '''


class Dia(models.Model):
    dia = models.CharField(verbose_name=_('Día'), null=False, unique=True, max_length=15)
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)

    def __str__(self):
        return self.dia


class Horario(models.Model):
    hora_inicio = models.TimeField(verbose_name=_('Hora Inicio'))
    hora_fin = models.TimeField(verbose_name=_('Hora Fin'))
    dias = models.ManyToManyField('Dia', verbose_name=_('Días'))
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)

    def __str__(self):
        i = 0
        total = len(self.dias.all())
        result = ''
        for dia in self.dias.all():
            result += dia.dia
            if i != total - 1:
                result += '-'
                i += 1
        result += ' ' + self.hora_inicio.__str__() + '-' + self.hora_fin.__str__()
        return result


class Grupo(models.Model):
    nombre = models.CharField(max_length=50, null=False, verbose_name=_('Nombre Grupo'), unique=True)
    horario = models.ForeignKey(Horario, on_delete=models.DO_NOTHING, verbose_name=_('Horario'), null=False)
    cantidad_encuestas = models.IntegerField(validators=[MinValueValidator(0)], null=False,
                                             verbose_name=_('Cantidad Máxima de Encuestas'), default=0)
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)

    def __str__(self):
        return self.nombre


class Cuestionario(models.Model):
    codigo = models.CharField(null=False, unique=True, verbose_name=_('Código Cuestionario'), max_length=10)
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)

    def __str__(self):
        return self.codigo


class Seccion(models.Model):
    nombre = models.CharField(max_length=25, null=False, verbose_name=_('Nombre Seccion'), unique=True)
    cuestionario = models.ForeignKey('Cuestionario', on_delete=models.DO_NOTHING, related_name=_('secciones'))
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)

    class Meta:
        verbose_name_plural = _('Secciones')

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    pregunta_espanol = models.TextField(null=False, verbose_name=_('Pregunta Espanol'))
    pregunta_ingles = models.TextField(null=False, verbose_name=_('Pregunta Ingés'))
    institucional = models.BooleanField(verbose_name=_('Pregunta Institucional'), default=False)
    seccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING, related_name='preguntas', null=True)
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)

    def __str__(self):
        return self.pregunta_espanol


class Registro(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.DO_NOTHING, verbose_name=_('Cuestionario'))
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING, verbose_name=_('Grupo'))
    profesor = models.ForeignKey(Profesor, on_delete=models.DO_NOTHING, verbose_name=_('Profesor'))
    comentario = models.TextField(verbose_name=_('Comentario'))
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)


class Respuesta(models.Model):
    pregunta = models.ForeignKey('Pregunta', on_delete=models.DO_NOTHING)
    respuesta = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    registro = models.ForeignKey('Registro', on_delete=models.DO_NOTHING, related_name=_('respuestas'))
    habilitado = models.BooleanField(verbose_name='Habilitado', default=True)
    creado_en = models.DateField(_("Fecha Creado"), default=datetime.date.today)
    actualizado_en = models.DateField(_("Fecha Ultima Actualizacion"), default=datetime.date.today)


class Configuracion(models.Model):
    nombre = models.CharField(verbose_name='Nombre Configuracion', max_length=25, null=False, unique=True)
    valor = models.CharField(verbose_name='Valor Configuracion', max_length=25, null=False, unique=False)

    class Meta:
        verbose_name_plural = _('Configuraciones')

    def __str__(self):
        return self.nombre
