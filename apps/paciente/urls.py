from django.urls import path
from django.conf.urls import url, include
from apps.paciente.views import PacienteCreate, PacienteList, PacienteUpdate, ModificarUpdate
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',login_required(PacienteCreate.as_view()), name='paciente_crear'),
    url(r'^listar',login_required(PacienteList.as_view()), name='paciente_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(PacienteUpdate.as_view()), name='paciente_editar'),
    url(r'^modificar/(?P<pk>\d+)/$',login_required(ModificarUpdate.as_view()), name='paciente_modificar'),
    
   ]