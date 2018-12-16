from django.core.management import BaseCommand

from webapp.models import Cuestionario, Seccion, Pregunta


class Command(BaseCommand):
    help = 'Crea las preguntas en la base de datos.'

    def handle(self, *args, **options):
        cuestionario = Cuestionario.objects.get_or_create(codigo='PROF1')
        seccion_profesor = Seccion.objects.get_or_create(nombre='Profesor', cuestionario=cuestionario[0])

        a = Pregunta.objects.get_or_create(pregunta_espanol='Es puntual.', pregunta_ingles='Is punctual.',
                                           seccion=seccion_profesor[0])
        b = Pregunta.objects.get_or_create(pregunta_espanol='Es dinámico.', pregunta_ingles='Is dynamic.',
                                           seccion=seccion_profesor[0])
        c = Pregunta.objects.get_or_create(pregunta_espanol='Comienza la clase con dinámica.',
                                           pregunta_ingles='Explains the class satisfactorily.',
                                           seccion=seccion_profesor[0])
        d = Pregunta.objects.get_or_create(pregunta_espanol='Explica satisfactoriamente.',
                                           pregunta_ingles='Explains the class satisfactorily.',
                                           seccion=seccion_profesor[0])
        e = Pregunta.objects.get_or_create(pregunta_espanol='Demuestra estar seguro de lo que enseña.',
                                           pregunta_ingles='Shows security on what he/she explains.',
                                           seccion=seccion_profesor[0])
        f = Pregunta.objects.get_or_create(pregunta_espanol='Involucra a todos en clase.',
                                           pregunta_ingles='Involucra a todos en clase.', seccion=seccion_profesor[0])
        g = Pregunta.objects.get_or_create(pregunta_espanol='Motiva a los estudiantes a participar.',
                                           pregunta_ingles='Motivates students to participate.',
                                           seccion=seccion_profesor[0])
        h = Pregunta.objects.get_or_create(pregunta_espanol='Utiliza otros recursos además de libros.',
                                           pregunta_ingles='Extends the book knowledge with other resources.',
                                           seccion=seccion_profesor[0])
        i = Pregunta.objects.get_or_create(
            pregunta_espanol='Se enfoca los 4 aspectos básicos: grámatica, lectura, escritura y expresión oral del '
                             'idioma.',
            pregunta_ingles='Focuses on the 4 basic aspects: speaking, writing, listening and reading.',
            seccion=seccion_profesor[0])
        j = Pregunta.objects.get_or_create(pregunta_espanol='Adapta los temas a la vida real.',
                                           pregunta_ingles='Adapts the topic to the real life.',
                                           seccion=seccion_profesor[0])
        k = Pregunta.objects.get_or_create(
            pregunta_espanol='Utiliza recursos audiovisuales evitando que los estudiantes se acostumbren a solo la '
                             'pronunciación.',
            pregunta_ingles='Uses audio and visual resources very frequently, avoiding students getting used only to '
                            'his/her pronunctiation.', seccion=seccion_profesor[0])
        l = Pregunta.objects.get_or_create(
            pregunta_espanol='Estimula al trabajo en grupo para que los estudiantes interactúen entre si.',
            pregunta_ingles='Stimulates working in groups, therefore the students can interact with each '
                            'other.', seccion=seccion_profesor[0])
        m = Pregunta.objects.get_or_create(
            pregunta_espanol='Estimula a los estudiantes a dar razones y ejemplos que apoyen su opinión utilizando la '
                             'gramática y vocabulario aprendidos.',
            pregunta_ingles='Stimulates students to give reasons and examples to support their opinions by using the '
                            'grammar they have learned.',
            seccion=seccion_profesor[0])

        n = Pregunta.objects.get_or_create(pregunta_espanol='Asigna y corrige tareas y trabajos de investigación.',
                                           pregunta_ingles="Assign and corrects homeworks and investigative reports.",
                                           seccion=seccion_profesor[0])

        o = Pregunta.objects.get_or_create(
            pregunta_espanol='Trabaja los ejercicios más importantes del workbook en el aula.',
            pregunta_ingles='Works on the most important exercises of the Workbook in the classroom.',
            seccion=seccion_profesor[0])
        p = Pregunta.objects.get_or_create(pregunta_espanol='Repite lo que los estudiantes preguntan sin objeción.',
                                           pregunta_ingles='Repeats what students ask without objection.',
                                           seccion=seccion_profesor[0])
        q = Pregunta.objects.get_or_create(pregunta_espanol='Corrige los errores de los estudiantes.',
                                           pregunta_ingles="Corrects the students' mistake.",
                                           seccion=seccion_profesor[0])
        r = Pregunta.objects.get_or_create(
            pregunta_espanol='Demuestra interés y preocupación por cada uno de los estudiantes.',
            pregunta_ingles='Demonstrate interest in and concern for each student.',
            seccion=seccion_profesor[0])
        s = Pregunta.objects.get_or_create(pregunta_espanol='Proyecta una imagen positiva y amigable.',
                                           pregunta_ingles='Projects a friendly and positive attitude in the classroom.',
                                           seccion=seccion_profesor[0])
        t = Pregunta.objects.get_or_create(pregunta_espanol='Permite el uso del español solamente en casos especiales.',
                                           pregunta_ingles='Speaks Spanish only in special situations.',
                                           seccion=seccion_profesor[0])
        u = Pregunta.objects.get_or_create(pregunta_espanol='Habla en inglés la mayoría del tiempo.',
                                           pregunta_ingles='Speaks English most of the time.',
                                           seccion=seccion_profesor[0])

        seccion_institucion = Seccion.objects.get_or_create(nombre='Institucion', cuestionario=cuestionario[0])

        inst_a = Pregunta.objects.get_or_create(pregunta_espanol='Nos brinda calidad en su servicio.',
                                                pregunta_ingles='Brings high quality service.', institucional=True,
                                                seccion=seccion_institucion[0])
        inst_b = Pregunta.objects.get_or_create(pregunta_espanol='El método satisface mis expectativas.',
                                                pregunta_ingles='The method is satisfactory.', institucional=True,
                                                seccion=seccion_institucion[0])
