from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView

from webapp.models import Profesor, Grupo, Cuestionario, Registro, Respuesta, Pregunta


class SeleccionarIdiomaTemplateView(TemplateView):
    template_name = 'evaluaciones/idioma.html'


class RealizarRegistroFormView(View):
    template_name = 'evaluaciones/realizar.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        context['idioma'] = self.request.GET['lang']
        context['profesores'] = Profesor.objects.filter(habilitado=True)
        context['grupos'] = Grupo.objects.filter(habilitado=True)
        context['cuestionario'] = Cuestionario.objects.filter(codigo=request.GET['codigo']).first()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        ok = False

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
