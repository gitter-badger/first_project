from django.shortcuts import render
from django.http import HttpResponseBadRequest
from forms import MyForm
import models
from datetime import datetime

def index(request):
    if request.user.is_authenticated():
        context = {"username": request.user.username}
        return render(request, 'create_form/create_form_template.html', context)
    else:
        return render(request, 'error_not_logged_in.html')

def date_time_to_datetime(date, time):
    date_ = datetime.strptime(date, "%Y-%m-%d").date()
    time_ = datetime.strptime(time, "%H:%M").time()
    return datetime.combine(date_, time_)

def map_form_to_database(form_dict, request):
    status = models.Status(name="brak")
    status.save()
    category = models.Category(name=form_dict["inputCategory"])
    category.save()
    title = form_dict["inputLocation"]
    max_participants = form_dict["inputMaxParticipants"]
    price = form_dict["inputPrice"]
    location = form_dict["inputLocation"]
    date = form_dict["inputFrom"]
    time = form_dict["inputFromTime"]
    start_date = date_time_to_datetime(date,time)
    date_to = form_dict["inputTo"]
    time_to = form_dict["inputToTime"]
    end_date = date_time_to_datetime(date_to, time_to)
    description = form_dict["inputDescription"]
    user = models.User.objects.get(username=request.user.username)
    event = models.Event( user=user,
                          status=status,
                          category=category,
                          title=title,
                          max_participants=max_participants,
                          price=price,
                          location=location,
                          start_date=start_date,
                          end_date=end_date,
                          description=description)
    event.save()
    return event.id

def form_creation(request):
    #try:
    pst = request.POST
    form = MyForm(pst)
    if not form.is_valid():
        raise ValueError(form.errors)       ##TODO better error
    event_id = map_form_to_database(form.cleaned_data, request) ##TODO proper link
    context = {"username": request.user.username, "form_link":  str(models.Event.objects.all())}
    #except ValueError as e:
    #    return HttpResponseBadRequest(str(e))
    #else:
    return render(request, 'create_form/form_created.html', context)