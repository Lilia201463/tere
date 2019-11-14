from django.urls import path
from django.conf.urls import url, include
from apps.pruebaPCR.views import  PruebaCreate, PruebaList, PruebaUpdate, PruebaDelete
urlpatterns = [
    url(r'^$',PruebaCreate.as_view(), name='prueba_crear'),
    url(r'^listar',PruebaList.as_view(), name='prueba_listar'),
    url(r'^editar/(?P<pk>\d+)/$',PruebaUpdate.as_view(), name='prueba_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',PruebaDelete.as_view(), name='prueba_eliminar'),
   ]