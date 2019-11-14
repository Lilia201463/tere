from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.cuestionario.forms import CuestionarioForm
from apps.cuestionario.models import Cuestionario
from django.urls import reverse_lazy 


class CuestionarioList(ListView):
	model = Cuestionario
	template_name = 'cuestionario/cuestionario_list.html'

class CuestionarioCreate(CreateView):
	model = Cuestionario
	form_class = CuestionarioForm
	template_name = 'cuestionario/cuestionario_form.html'
	success_url = reverse_lazy('cuestionario:cuestionario_listar')


class CuestionarioUpdate(UpdateView):
	model = Cuestionario
	form_class = CuestionarioForm
	template_name = 'cuestionario/cuestionario_form.html'
	success_url = reverse_lazy('cuestionario:cuestionario_listar')



class CuestionarioDelete(DeleteView):
	model = Cuestionario
	template_name = 'cuestionario/cuestionario_delete.html'
	success_url = reverse_lazy('cuestionario:cuestionario_listar')
