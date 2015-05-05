from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def index(request):
    text = "hello world"
    title = "First template"
    context_dict = {'text': text, 'title': title}
    return render(request, 'login/index.html', context_dict)


def auth(request):
    username = request.POST['inputEmail']
    password = request.POST['inputPassword']
    user = authenticate(email=username, password=password)
    print user
    if user is not None:
        login(request, user)
        return render(request, 'login/success.html', {"username": username, "password": password})
    return render(request, 'login/failed.html', {"username": username, "password": password})