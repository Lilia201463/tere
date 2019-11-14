from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.expediente.forms import ExpedienteForm
from apps.expediente.models import Expediente
from django.urls import reverse_lazy 
# Create your views here.
class ExpedienteList(ListView):
	model = Expediente
	template_name = 'expediente/expediente_list.html'

class ExpedienteCreate(CreateView):
	model = Expediente
	form_class = ExpedienteForm
	template_name = 'expediente/expediente_form.html'
	success_url = reverse_lazy('expediente:expediente_listar')


class ExpedienteUpdate(UpdateView):
	model = Expediente
	form_class = ExpedienteForm
	template_name = 'expediente/expediente_form.html'
	success_url = reverse_lazy('expediente:expediente_listar')



class ExpedienteDelete(DeleteView):
	model = Expediente
	template_name = 'expediente/expediente_delete.html'
	success_url = reverse_lazy('expediente:expediente_listar')