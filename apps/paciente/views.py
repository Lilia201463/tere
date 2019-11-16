from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from apps.paciente.forms import PacienteForm
from apps.paciente.models import Paciente
from django.urls import reverse_lazy 
# Create your views here.
class PacienteList(ListView):
	model = Paciente
	template_name = 'paciente/paciente_list.html'

class PacienteCreate(CreateView):
	model = Paciente
	form_class = PacienteForm
	template_name = 'paciente/paciente_form.html'
	success_url = reverse_lazy('paciente:paciente_listar')


class PacienteUpdate(UpdateView):
	model = Paciente
	form_class = PacienteForm
	template_name = 'paciente/paciente_form.html'
	success_url = reverse_lazy('paciente:paciente_listar')

class ModificarUpdate(UpdateView):
	model = Paciente
	form_class = PacienteForm
	template_name = 'paciente/index_paciente.html'
	success_url = reverse_lazy('paciente:paciente_listar')


