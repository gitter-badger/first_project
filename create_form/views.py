from django.shortcuts import render
from django.http import Http404


def index(request):
    text = "html exists"
    title = "create_form_template"
    context_dict = {'text':text,'title':title}
    return render(request, 'create_form/create_form_template.html', context_dict)
