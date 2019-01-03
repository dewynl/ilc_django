from django.core.management import BaseCommand

from webapp.models import Configuracion


class Command(BaseCommand):
    help = 'Comando para crear en la BD las configuraciones default del sistema.'

    def handle(self, *args, **options):

        try:
            conf = Configuracion.objects.get_or_create(nombre='encuestas_activadas', valor='true')
            print(conf.nombre)
        except Exception as e:
            raise e
