from django.shortcuts import render
from django.http import HttpResponseBadRequest
from forms import MyForm
import models


def index(request):
    if request.user.is_authenticated():
        context = {"username": request.user.username}
        return render(request, 'create_form/create_form_template.html', context)
    else:
        return render(request, 'error_not_logged_in.html')

def map_form_to_database(form):
    models.Event()
    pass

def form_creation(request):
    try:
        pst = request.POST
        form = MyForm(pst, extra=len(pst))
        if not form.is_valid():
            raise ValueError(form.errors)       ##TODO better error
        resulting_link = map_form_to_database(form)
        context = {"username": request.user.username, "form_link": str(form.cleaned_data["inputEventTitle"])}
    except ValueError as e:
        return HttpResponseBadRequest(str(e))
    else:
        return render(request, 'create_form/form_created.html', context)