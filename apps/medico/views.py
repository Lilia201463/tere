from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.medico.forms import MedicoForm
from apps.medico.models import Medico
from django.urls import reverse_lazy 

class MedicoList(ListView):
	model = Medico
	template_name = 'medico/medico_list.html'

class MedicoCreate(CreateView):
	model = Medico
	form_class = MedicoForm
	template_name = 'medico/medico_form.html'
	success_url = reverse_lazy('medico:medico_listar')


class MedicoUpdate(UpdateView):
	model = Medico
	form_class = MedicoForm
	template_name = 'medico/medico_form.html'
	success_url = reverse_lazy('medico:medico_listar')



class MedicoDelete(DeleteView):
	model = Medico
	template_name = 'medico/medico_delete.html'
	success_url = reverse_lazy('medico:medico_listar')

def index(request):
	return render(request, 'medico/index.html')
