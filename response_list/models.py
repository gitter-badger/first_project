from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from create_form.models import Event
from form_response.models import RegistrationInstance


class ParticipantForm(ModelForm):
    class Meta:
        model = RegistrationInstance
        fields = ['name', 'last_name', 'email', 'registration_confirmed'] #TODO add events and gifts
