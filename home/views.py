from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from create_form.models import Event


def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})