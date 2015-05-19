from django.shortcuts import render
import models

def event_list(request):
    if request.user.is_authenticated():
        user = models.User(id=request.user.id)
        events = models.Event.objects.filter(user=user)
        context = {"events": events}
        return render(request, 'response_list/event_list.html', context)
    else:
        raise ValueError() #TODO better error

def index(request):
    if request.user.is_authenticated():
        user = models.User(id=request.user.id)
        event_id = request.GET["event_id"]
        event = models.Event.objects.get(id=event_id, user=user)
        registration = models.RegistrationInstance.objects.filter(event=event)
        form_link = "../form_response/?id="+str(event_id)
        context = {"participants": registration,"form_link":form_link}
        return render(request, 'response_list/basic_response_list.html',context)
    else:
        raise ValueError() #TODO better error
