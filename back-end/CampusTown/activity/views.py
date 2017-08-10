# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .models import ActivityInfo,ActivityLanguage
from .forms import ActivityForm, ActivityLanguageForm

class host2_category(FormView):
	templat_name='host2.html'
	success_url='/success/'
	form_class=ActivityForm

	def form_valid(self, form):
		return HttpResponse("input success.")

class host2_language(FormView):
	template_name='host2.html'
	success_url='/success/'
	form_class=ActivityLanguageForm
	
	def form_valid(self, form):
		return HttpResponse("input success.")

#class host0(FormView):

#class host1(FormView):

#class host3(FormView):

#class host4(FormView):

#class host5(FormView):

#class host6(FormView):

#class host7(FormView):

#class host8(FormView):


