"""ilc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.admins.views import IndexView, ProfesoresListView, CrearProfesorFormView, EditarProfesorFormView, \
    HorariosListView, CrearHorarioFormView, EditarHorarioFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', IndexView.as_view(), name='admins-index'),
    #PROFESORES
    path('admins/profesores/', ProfesoresListView.as_view(), name='profesores-index'),
    path('admins/profesores/crear/', CrearProfesorFormView.as_view(), name='profesores-crear'),
    path('admins/profesores/editar/<int:pk>', EditarProfesorFormView.as_view(), name='profesores-editar'),
    #HORARIOS
    path('admins/horarios/', HorariosListView.as_view(), name='horarios-index'),
    path('admins/horarios/crear/', CrearHorarioFormView.as_view(), name='horarios-crear'),
    path('admins/horarios/editar/<int:pk>', EditarHorarioFormView.as_view(), name='horarios-editar'),
]
