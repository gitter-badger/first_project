from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext


def index(request):
    return render(request, 'login/index.html')


def auth(request):
    username = request.POST['inputEmail']
    password = request.POST['inputPassword']
    user = authenticate(email=username, password=password)
    print user
    if user is not None:
        login(request, user)
    return HttpResponseRedirect('/')


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/')