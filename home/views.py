from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from django.contrib.auth.decorators import login_required  # used in function base decorative
from django.contrib.auth.mixins import LoginRequiredMixin  # used in class base view

from django.contrib.auth.views import LoginView, LogoutView

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