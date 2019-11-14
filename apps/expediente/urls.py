from django.urls import path
from django.conf.urls import url, include
from apps.expediente.views import ExpedienteCreate, ExpedienteList, ExpedienteUpdate, ExpedienteDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',login_required(ExpedienteCreate.as_view()), name='expediente_crear'),
    url(r'^listar',login_required(ExpedienteList.as_view()), name='expediente_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(ExpedienteUpdate.as_view()), name='expediente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(ExpedienteDelete.as_view()), name='expediente_eliminar'),
   ]