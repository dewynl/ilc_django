from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from ilc import settings
from webapp.admins.forms import ProfesorForm, HorarioForm, GrupoForm
from webapp.models import Profesor, Horario, Grupo


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = settings.ADMIN_LOGIN_URL
    template_name = 'admins/index.html'


class ProfesoresListView(ListView):
    model = Profesor
    template_name = 'admins/profesores/profesores-list.html'


class CrearProfesorFormView(CreateView):
    model = Profesor
    template_name = 'admins/profesores/profesores-form.html'
    success_url = reverse_lazy('profesores-index')
    form_class = ProfesorForm


class EditarProfesorFormView(UpdateView):
    model = Profesor
    template_name = 'admins/profesores/profesores-form.html'
    success_url = reverse_lazy('profesores-index')
    form_class = ProfesorForm


class HorariosListView(ListView):
    model = Horario
    template_name = 'admins/horarios/horarios-list.html'


class CrearHorarioFormView(CreateView):
    model = Horario
    template_name = 'admins/horarios/horarios-form.html'
    success_url = reverse_lazy('horarios-index')
    form_class = HorarioForm


class EditarHorarioFormView(UpdateView):
    model = Horario
    template_name = 'admins/horarios/horarios-form.html'
    success_url = reverse_lazy('horarios-index')
    form_class = HorarioForm


class GruposListView(ListView):
    model = Grupo
    template_name = 'admins/grupos/grupos-list.html'


class CrearGruposFormView(CreateView):
    model = Grupo
    template_name = 'admins/grupos/grupos-form.html'
    success_url = reverse_lazy('grupos-index')
    form_class = GrupoForm


class EditarGruposFormView(UpdateView):
    model = Grupo
    template_name = 'admins/grupos/grupos-form.html'
    success_url = reverse_lazy('grupos-index')
    form_class = GrupoForm
