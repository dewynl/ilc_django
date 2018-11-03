from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ilc import settings


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = settings.ADMIN_LOGIN_URL
    template_name = 'admins/index.html'
