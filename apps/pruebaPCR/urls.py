from django.urls import path
from django.conf.urls import url, include
from apps.pruebaPCR.views import  PruebaCreate, PruebaList, PruebaUpdate, PruebaDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',login_required(PruebaCreate.as_view()), name='prueba_crear'),
    url(r'^listar',login_required(PruebaList.as_view()), name='prueba_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(PruebaUpdate.as_view()), name='prueba_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(PruebaDelete.as_view()), name='prueba_eliminar'),
   ]