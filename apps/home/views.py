from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.home.forms import HomeForm
from apps.home.models import Home
from django.urls import reverse_lazy 

class HomeList(ListView):
	model = Home
	template_name = 'home/home_list.html'

class HomeCreate(CreateView):
	model = Home
	form_class = HomeForm
	template_name = 'home/home_form.html'
	success_url = reverse_lazy('home:home_listar')


class HomeUpdate(UpdateView):
	model = Home
	form_class = HomeForm
	template_name = 'home/home_form.html'
	success_url = reverse_lazy('home:home_listar')



class HomeDelete(DeleteView):
	model = Home
	template_name = 'home/home_delete.html'
	success_url = reverse_lazy('home:home_listar')


