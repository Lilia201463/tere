"""propio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/', include(('apps.home.urls','apps.home'),namespace='home')),
    url(r'^paciente/', include(('apps.paciente.urls','apps.paciente'),namespace='paciente')),
    url(r'^medico/', include(('apps.medico.urls','apps.medico'),namespace='medico')),
    url(r'^cuestionario/', include(('apps.cuestionario.urls','apps.cuestionario'),namespace='cuestionario')),
    url(r'^expediente/', include(('apps.expediente.urls','apps.expediente'),namespace='expediente')),
    url(r'^pruebaPCR/', include(('apps.pruebaPCR.urls','apps.pruebaPCR'),namespace='pruebaPCR')),
    url(r'^usuario/', include(('apps.usuario.urls','apps.usuario'),namespace='usuario')),
    url(r'^login/', LoginView.as_view(template_name='index.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(template_name='base:base.html'), name='logout'),
    url(r'^reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name= 'registration/password_reset_email.html'), name='password_reset'), 
    url(r'^password_reset_done', PasswordResetDoneView.as_view(template_name= 'registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name= 'registration/password_reset_confirm.html'),name='password_reset_confirm'),
    url(r'^reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
