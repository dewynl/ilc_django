from django.forms import ModelForm

from webapp.models import Profesor, Horario


class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese nombre del profesor'})


class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['hora_inicio', 'hora_fin', 'dias', ]

    def __init__(self, *args, **kwargs):
        super(HorarioForm, self).__init__(*args, **kwargs)
        self.fields['hora_inicio'].widget.attrs.update(
            {'class': 'form-control pickatime', 'placeholder': 'Ingrese hora de inicio'})
        self.fields['hora_fin'].widget.attrs.update(
            {'class': 'form-control pickatime', 'placeholder': 'Ingrese hora fin'})
        self.fields['dias'].widget.attrs.update(
            {'class': 'form-control select', 'multiple': 'multiple', 'style': 'width: 100%'})
