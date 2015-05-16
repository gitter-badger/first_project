from django import forms
from django.forms import model_to_dict
from django.shortcuts import render
# Create your views here.
from form_response.models import FormField, RegistrationForm, EventDetails
from login.typeHelper import convert_string_to_type


def index(request):
    event = EventDetails(1, 'testTITle', 'mountains', 'Open', 150, 50, 15.23, 'zadupie', '11-04-2015 11:00', '12-04-2015 13:00',
                         'taki tam description')  # tu bedzie get eventu z bazy (po id z requesta)
    sth = [FormField('name', True, 'CharField'), FormField('Date', False, 'DateTimeField')]
    attrs = {}
    for field in sth:
        attrs.__setitem__(field.name, convert_string_to_type(field.type))
    form = type("RegistrationForm", (RegistrationForm,), attrs)  # tu bedzie get pol z bazy (po id eventu z bazy)
    return render(request, 'register.html', {'event': event, 'form': form})

