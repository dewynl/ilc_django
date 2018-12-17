from bootstrap_datepicker_plus import TimePickerInput
from django.forms import ModelForm
from django import forms

from webapp.models import Profesor, Horario, Grupo


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, min_length=5, widget={})
    password = forms.CharField(widget=forms.PasswordInput())


class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'habilitado']

    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese nombre del profesor'})
        self.fields['habilitado'].widget.attrs.update({'class': '', })


class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['hora_inicio', 'hora_fin', 'dias', 'habilitado', ]
        widgets = {
            'hora_inicio': TimePickerInput(),
            'hora_fin': TimePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        super(HorarioForm, self).__init__(*args, **kwargs)
        self.fields['hora_inicio'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese hora de inicio'})
        self.fields['hora_fin'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese hora fin'})
        self.fields['dias'].widget.attrs.update(
            {'class': 'form-control select', 'multiple': 'multiple', 'style': 'width: 100%'})
        self.fields['habilitado'].widget.attrs.update(
            {'class': '', })


class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'horario', 'habilitado', ]

    def __init__(self, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese nombre del grupo'})
        self.fields['horario'].widget.attrs.update({'class': 'form-control select', 'style': 'width: 100%'})
        self.fields['habilitado'].widget.attrs.update({'class': '', })
