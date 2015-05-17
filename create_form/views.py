from django.shortcuts import render
from django.http import Http404


def index(request):
    if request.user.is_authenticated():
        context = {"username": request.user.username}
        return render(request, 'create_form/create_form_template.html', context)
    else:
        return render(request, 'error_not_logged_in.html')
