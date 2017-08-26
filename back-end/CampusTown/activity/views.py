# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic import TemplateView
from .models import ActivityInfo
from .forms import ActivityForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

def host2(request):
	if request.method=="POST":
		form=ActivityForm(request.POST)
		if form.is_valid():
			new_activity=form.save(commit=False)
			new_activity.save()
			return redirect('host4')
	else:
		form=ActivityForm()
	return render(request,'activity/host2.html',{'form':form})
	
def host4(request):
	return render(request,'activity/host4.html',) 

def host1(request):
	return render(request,'activity/host1.html',{})	

def host8(request,pk):
	activity=get_object_or_404(ActivityInfo,pk=pk)
	context={"new_activity":activity}
	return render(request,'activity/host8.html',context)

def host5(request):
	return render(request,'activity/host5.html')

def host9(request):
	#if request.method=="POST":
	#	form=ActivityForm(request.POST)
	#	if form.is_valid():
	return render(request,'activity/host9.html')

#class host0(FormView):
	

#class host3(FormView):

#class host4(FormView):

#class host5(FormView):

#class host6(FormView):

#class host7(FormView):


def hostN(request):
	return render(request,'activity/hostN.html')

