from django.urls import path
from django.conf.urls import url, include
from apps.expediente.views import ExpedienteCreate, ExpedienteList, ExpedienteUpdate, ExpedienteDelete
urlpatterns = [
    url(r'^$',ExpedienteCreate.as_view(), name='expediente_crear'),
    url(r'^listar',ExpedienteList.as_view(), name='expediente_listar'),
    url(r'^editar/(?P<pk>\d+)/$',ExpedienteUpdate.as_view(), name='expediente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',ExpedienteDelete.as_view(), name='expediente_eliminar'),
   ]
