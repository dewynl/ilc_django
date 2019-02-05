from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from datetime import datetime

from webapp.models import Profesor, Grupo, Cuestionario, Registro, Respuesta, Pregunta, Configuracion


class SeleccionarIdiomaTemplateView(TemplateView):
    template_name = 'evaluaciones/idioma.html'

    def get_context_data(self, **kwargs):
        context = super(SeleccionarIdiomaTemplateView, self).get_context_data(**kwargs)
        context['activada'] = Configuracion.objects.filter(nombre='encuestas_activadas', valor='true').exists()
        return context


class RealizarRegistroFormView(View):
    template_name = 'evaluaciones/realizar.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        context['idioma'] = self.request.GET['lang']
        context['activada'] = Configuracion.objects.filter(nombre='encuestas_activadas', valor='true').exists()

        if context['activada']:
            now = datetime.now()
            context['profesores'] = Profesor.objects.filter(habilitado=True)
            context['grupos'] = []

            grupos = Grupo.objects.filter(habilitado=True)
            for grupo in grupos:
                cantidad_registros = Registro.objects.filter(creado_en__gte=datetime(now.year, now.month, now.day),
                                                             creado_en__lte=datetime(now.year, now.month, now.day + 1),
                                                             grupo=grupo).count()
                if cantidad_registros < grupo.cantidad_encuestas:
                    context['grupos'].append(grupo)

            context['cuestionario'] = Cuestionario.objects.filter(codigo=request.GET['codigo']).first()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ok = False

        with transaction.atomic():
            try:
                cuestionario = Cuestionario.objects.filter(id=request.POST['cuestionario']).first()
                profesor = Profesor.objects.filter(id=request.POST['profesor']).first()
                grupo = Grupo.objects.filter(id=request.POST['grupo']).first()
                comentario = request.POST['comentario']
                registro = Registro.objects.create(cuestionario=cuestionario, profesor=profesor, grupo=grupo,
                                                   comentario=comentario)
                for key in request.POST.keys():
                    if 'preg' in key:
                        pregunta = Pregunta.objects.filter(id=key.split('_')[1]).first()
                        respuesta = Respuesta.objects.create(pregunta=pregunta, registro=registro,
                                                             respuesta=request.POST[key])
                ok = True
            except Exception as e:
                raise str(e)

        return redirect('/registro/realizado/?ok=' + str(ok))


class RegistroRealizadoTemplateView(TemplateView):
    template_name = 'evaluaciones/realizado.html'

    def get_context_data(self, **kwargs):
        context = super(RegistroRealizadoTemplateView, self).get_context_data(**kwargs)
        context['ok'] = self.request.GET['ok']
        return context
