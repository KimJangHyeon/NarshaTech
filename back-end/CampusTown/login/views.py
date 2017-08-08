from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Login failed. Try again.')
            return HttpResponse("")
    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})