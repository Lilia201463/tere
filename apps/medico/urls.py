from django.urls import path
from django.conf.urls import url, include
from apps.medico.views import MedicoCreate, MedicoList, MedicoUpdate, MedicoDelete, index
urlpatterns = [
    url(r'^$',MedicoCreate.as_view(), name='medico_crear'),
    url(r'^listar',MedicoList.as_view(), name='medico_listar'),
    url(r'^editar/(?P<pk>\d+)/$',MedicoUpdate.as_view(), name='medico_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',MedicoDelete.as_view(), name='medico_eliminar'),
    url(r'^inicio$', index, name='medico_inicio'),
   ]