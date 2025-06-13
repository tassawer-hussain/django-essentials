from django.shortcuts import render, redirect
from django.http import HttpResponse

from datetime import datetime
from django.contrib.auth.decorators import login_required  # used in function base decorative
from django.contrib.auth.mixins import LoginRequiredMixin  # used in class base view

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     # return HttpResponse('Hello, world!')
#     return render(request,  'home/welcome.html', { 'today': datetime.today()})

# @login_required(login_url='admin/')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = { 'today': datetime.today() }

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = 'admin/'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})