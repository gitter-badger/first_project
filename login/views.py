from django.shortcuts import render

def index(request):
    text = "hello world"
    title = "First template"
    context_dict = {'text':text,'title':title}
    return render(request, 'login/index.html', context_dict)
