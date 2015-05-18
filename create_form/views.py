from django.shortcuts import render
from django.http import HttpResponseBadRequest


def index(request):
    if request.user.is_authenticated():
        context = {"username": request.user.username}
        return render(request, 'create_form/create_form_template.html', context)
    else:
        return render(request, 'error_not_logged_in.html')


def form_creation(request):
    try:
        pst = request.POST

        context = {"username": request.user.username, "form_link": str(pst)}
    except ValueError:
        return HttpResponseBadRequest("invalid input value")
    else:
        return render(request, 'create_form/form_created.html', context)