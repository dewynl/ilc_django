from django.contrib import admin

from webapp.models import Profesor, Grupo, Horario, Dia


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


admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Dia, DiaAdmin)
