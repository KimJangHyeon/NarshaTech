# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic import TemplateView
from .models import ActivityInfo
from .forms import ActivityForm
from django.shortcuts import render, redirect


def host2(request):
	if request.method=='POST':
	
		form=ActivityForm(request.POST)
		if form.is_valid():

			category=form.cleaned_data["category"]
			language=form.cleaned_data["language"]
			new_activity=ActivityInfo(category=category, language=language)
			new_activity.save()

			return HttpResponseRedirect(reverse('host2'))
	else:
		form=ActivityForm()

	return render(request,'activity/host2.html',{'form':form},)
	
def host4(request):
	return render(request,'activity/host4.html',{'form':form}) 

def host1(request):
	return render(request,'activity/host1.html',{})	

def host5(request):
	return render(request,'activity/host5.html',{})

def host4(request):
	return render(request,'activity/host4.html',{})
#class host0(FormView):
	

#class host3(FormView):

#class host4(FormView):

#class host5(FormView):

#class host6(FormView):

#class host7(FormView):

#class host8(FormView):


