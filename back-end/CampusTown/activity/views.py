# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .models import ActivityInfo
from .forms import ActivityForm


#class host2_category(FormView):
#	templat_name='host2.html'
#	success_url='/success/'
#	form_class=ActivityForm
#
#	def form_valid(self, form):
#		return HttpResponse("input success.")

def host2(request):
	if request.method=="POST":
		form=ActivityForm(request.POST)
		if form.is_valid():
			new_activity=ActivityInfo.objects.create(category=form.cleaned_data['category'],language=form.cleaned_data['language'])
			new_activity.save()
			return HttpResponseRedirect('/')
	else:
		form=ActivityForm()
	return render(request,'activity/host2.html',{'form':form})	
 
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


