from django.shortcuts import redirect
from .models import *
from django.views.generic import CreateView
from activity.UserForm import *
# Create your views here.

def main_Page(request):
	return render(request,'activity/mainPage.html',{})

def sign_up(request):
	if request.method=='POST':
		form=UserFrom(request.POST)
		if form.is_valid():
			user=User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email'],
				type=form.cleaned_data['type'],
				last_name=form.cleaned_data['last_name'],
				first_name=form.cleaned_data['first_name'],
				birth=form.cleaned_data['birth'],
				phone=form.cleaned_data['phone'],
				gender=form.cleaned_data['gender']
				)
			
			user.save()
			return HttpResponseRedirect('/')
		else:
			form=UserForm()
		variables=RequestContext(request,{'form':form})
		return render_to_response('activity/sign_up.html',variables)
