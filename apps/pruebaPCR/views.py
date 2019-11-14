from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.pruebaPCR.forms import PruebaForm
from apps.pruebaPCR.models import Prueba_PCR
from django.urls import reverse_lazy 
# Create your views here.
class PruebaList(ListView):
	model = Prueba_PCR
	template_name = 'pruebaPCR/prueba_list.html'

class PruebaCreate(CreateView):
	model = Prueba_PCR
	form_class = PruebaForm
	template_name = 'pruebaPCR/prueba_form.html'
	success_url = reverse_lazy('pruebaPCR:prueba_listar')


class PruebaUpdate(UpdateView):
	model = Prueba_PCR
	form_class = PruebaForm
	template_name = 'pruebaPCR/prueba_form.html'
	success_url = reverse_lazy('pruebaPCR:prueba_listar')



class PruebaDelete(DeleteView):
	model = Prueba_PCR
	template_name = 'pruebaPCR/prueba_delete.html'
	success_url = reverse_lazy('pruebaPCR:prueba_listar')