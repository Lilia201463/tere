from django.urls import path
from django.conf.urls import url, include
from apps.home.views import HomeCreate, HomeList, HomeUpdate, HomeDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',HomeCreate.as_view(), name='home_crear'),
    url(r'^listar',login_required(HomeList.as_view()), name='home_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(HomeUpdate.as_view()), name='home_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(HomeDelete.as_view()), name='home_eliminar'),
   ]