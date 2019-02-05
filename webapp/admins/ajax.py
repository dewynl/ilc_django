from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.views import View

from webapp.models import Profesor, Registro


class ComentariosPorProfesorAjax(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        profesor = Profesor.objects.filter(id=request.GET['data']).first()
        registros = Registro.objects.filter(profesor=profesor).filter(habilitado=True)
        result = None
        if len(registros) > 0:
            result = [{}]
            for registro in registros:
                result.append({'comentario': registro.comentario})

        return self.render_json_response(result)


class PromedioPorProfesorAjax(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        profesor = Profesor.objects.filter(id=request.GET['data']).first()
        registros = Registro.objects.filter(profesor=profesor, habilitado=True)

        map = dict()
        for registro in registros:
            respuestas = registro.respuestas.filter(habilitado=True)
            for respuesta in respuestas:
                if not respuesta.pregunta.institucional:
                    if respuesta.pregunta.pregunta_espanol in map.keys():
                        map[respuesta.pregunta.pregunta_espanol] += respuesta.respuesta
                    else:
                        map[respuesta.pregunta.pregunta_espanol] = respuesta.respuesta

        for key, value in map.items():
            map[key] = value / len(registros)

        resp = {'respuestas': map, 'totalPregs': len(map)}
        return self.render_json_response(resp)


class PromedioInstitucionAjax(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        registros = Registro.objects.filter(habilitado=True)
        map = dict()
        for registro in registros:
            respuestas = registro.respuestas.filter(habilitado=True)
            for respuesta in respuestas:
                if respuesta.pregunta.institucional:
                    if respuesta.pregunta.pregunta_espanol in map.keys():
                        map[respuesta.pregunta.pregunta_espanol] += respuesta.respuesta
                    else:
                        map[respuesta.pregunta.pregunta_espanol] = respuesta.respuesta

        for key, value in map.items():
            map[key] = value / len(registros)

        resp = {'respuestas': map, 'totalPregs': len(map)}
        return self.render_json_response(resp)
