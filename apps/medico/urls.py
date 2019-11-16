from django.urls import path
from django.conf.urls import url, include
from apps.medico.views import MedicoCreate, MedicoList, MedicoUpdate, MedicoDelete, index
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',login_required(MedicoCreate.as_view()), name='medico_crear'),
    url(r'^listar',login_required(MedicoList.as_view()), name='medico_listar'),
    url(r'^editar/(?P<pk>[0-9A-Za-z]+)/$',login_required(MedicoUpdate.as_view()), name='medico_editar'),
    url(r'^eliminar/(?P<pk>[0-9A-Za-z]+)/$',login_required(MedicoDelete.as_view()), name='medico_eliminar'),
    url(r'^inicio$', login_required(index), name='medico_inicio'),
   ]