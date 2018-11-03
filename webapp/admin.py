from django.contrib import admin

from webapp.models import Profesor, Grupo, Horario


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'habilitado',)
    search_fields = ('nombre',)


class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'habilitado',)
    search_fields = ('nombre',)


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('hora_inicio', 'hora_fin', 'habilitado',)


admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Horario, HorarioAdmin)
