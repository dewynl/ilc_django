from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, RedirectView, FormView, View

from ilc import settings
from webapp.admins.forms import ProfesorForm, HorarioForm, GrupoForm, LoginForm
from webapp.models import Profesor, Horario, Grupo, Configuracion


class LogoutAdminView(RedirectView):
    pattern_name = 'admin-login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutAdminView, self).get(request, *args, **kwargs)


class AdminLoginFormView(FormView):
    template_name = "admins/login/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('admins-index')

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user and user.is_staff:
            login(self.request, user=user)
        return super(AdminLoginFormView, self).form_valid(form)


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = settings.ADMIN_LOGIN_URL
    template_name = 'admins/index.html'


class ProfesoresListView(LoginRequiredMixin, ListView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Profesor
    template_name = 'admins/profesores/profesores-list.html'


class CrearProfesorFormView(LoginRequiredMixin, CreateView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Profesor
    template_name = 'admins/profesores/profesores-form.html'
    success_url = reverse_lazy('profesores-index')
    form_class = ProfesorForm


class EditarProfesorFormView(LoginRequiredMixin, UpdateView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Profesor
    template_name = 'admins/profesores/profesores-form.html'
    success_url = reverse_lazy('profesores-index')
    form_class = ProfesorForm


class HorariosListView(LoginRequiredMixin, ListView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Horario
    template_name = 'admins/horarios/horarios-list.html'


class CrearHorarioFormView(LoginRequiredMixin, CreateView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Horario
    template_name = 'admins/horarios/horarios-form.html'
    success_url = reverse_lazy('horarios-index')
    form_class = HorarioForm


class EditarHorarioFormView(LoginRequiredMixin, UpdateView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Horario
    template_name = 'admins/horarios/horarios-form.html'
    success_url = reverse_lazy('horarios-index')
    form_class = HorarioForm


class GruposListView(LoginRequiredMixin, ListView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Grupo
    template_name = 'admins/grupos/grupos-list.html'


class CrearGruposFormView(LoginRequiredMixin, CreateView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Grupo
    template_name = 'admins/grupos/grupos-form.html'
    success_url = reverse_lazy('grupos-index')
    form_class = GrupoForm


class EditarGruposFormView(LoginRequiredMixin, UpdateView):
    login_url = settings.ADMIN_LOGIN_URL
    model = Grupo
    template_name = 'admins/grupos/grupos-form.html'
    success_url = reverse_lazy('grupos-index')
    form_class = GrupoForm


class EvaluacionesPorProfesorView(LoginRequiredMixin, TemplateView):
    login_url = settings.ADMIN_LOGIN_URL
    template_name = 'admins/evaluaciones/evaluacion-profesores.html'

    def get_context_data(self, **kwargs):
        context = super(EvaluacionesPorProfesorView, self).get_context_data(**kwargs)
        context['profesores'] = Profesor.objects.filter(habilitado=True)
        context['encuestas_activadas'] = Configuracion.objects.filter(nombre='encuestas_activadas',
                                                                      valor='true').exists()
        return context


class EvaluacionesALaInstitucionView(LoginRequiredMixin, TemplateView):
    login_url = settings.ADMIN_LOGIN_URL
    template_name = 'admins/evaluaciones/evaluacion-institucion.html'


class CambiarEstadoEvaluaciones(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        print(request.GET['estado'])
        conf = Configuracion.objects.filter(nombre='encuestas_activadas').first()
        conf.valor = request.GET['estado']
        conf.save()
        return redirect('/admins/evaluaciones/profesores/')

