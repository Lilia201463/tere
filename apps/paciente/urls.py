from django.urls import path
from django.conf.urls import url, include
from apps.paciente.views import PacienteCreate, PacienteList, PacienteUpdate, ModificarUpdate
urlpatterns = [
    url(r'^$',PacienteCreate.as_view(), name='paciente_crear'),
    url(r'^listar',PacienteList.as_view(), name='paciente_listar'),
    url(r'^editar/(?P<pk>\d+)/$',PacienteUpdate.as_view(), name='paciente_editar'),
    url(r'^modificar/(?P<pk>\d+)/$',ModificarUpdate.as_view(), name='paciente_modificar'),
    
   ]