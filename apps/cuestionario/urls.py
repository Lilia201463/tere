from django.urls import path
from django.conf.urls import url, include
from apps.cuestionario.views import CuestionarioCreate, CuestionarioList, CuestionarioUpdate, CuestionarioDelete
urlpatterns = [
    url(r'^$',CuestionarioCreate.as_view(), name='cuestionario_crear'),
    url(r'^listar',CuestionarioList.as_view(), name='cuestionario_listar'),
    url(r'^editar/(?P<pk>\d+)/$',CuestionarioUpdate.as_view(), name='cuestionario_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',CuestionarioDelete.as_view(), name='cuestionario_eliminar'),
   ]