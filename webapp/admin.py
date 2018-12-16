from django.contrib import admin

from webapp.models import Profesor, Grupo, Horario, Dia, Seccion, Cuestionario, Pregunta, Respuesta, Registro


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'habilitado', 'creado_en', 'actualizado_en',)
    search_fields = ('nombre',)


class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'habilitado', 'creado_en', 'actualizado_en',)
    search_fields = ('nombre', 'creado_en', 'actualizado_en',)


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('hora_inicio', 'hora_fin', 'habilitado', 'creado_en', 'actualizado_en',)


class DiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'dia', 'habilitado', 'creado_en', 'actualizado_en',)


class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuestionario', 'habilitado', 'creado_en', 'actualizado_en',)


class CuestionarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'habilitado', 'creado_en', 'actualizado_en',)


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'pregunta_espanol', 'pregunta_ingles', 'institucional', 'seccion', 'habilitado', 'creado_en',
                    'actualizado_en',)


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'respuesta', 'registro', 'habilitado', 'creado_en', 'actualizado_en',)


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'cuestionario', 'grupo', 'profesor', 'comentario', 'habilitado', 'creado_en', 'actualizado_en',)


admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Dia, DiaAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Cuestionario, CuestionarioAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Registro, RegistroAdmin)
