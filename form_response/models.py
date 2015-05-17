from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.forms import forms
from create_form.models import Event, Event_own_field, Event_gift


class RegistrationForm(forms.Form):
    pass


class Registration_instance(models.Model):
    registration_instance_id = models.AutoField(primary_key=True)
    event_assessment = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    event_fraudulent = models.BooleanField(default=False)
    registration_confirmed = models.BooleanField(default=False)
    event_id = models.ForeignKey(Event)

class Event_form_field_instance(models.Model):
    event_form_field_instance_id = models.AutoField(primary_key=True)
    event_form_field_id = models.ForeignKey(Event_own_field)
    value = models.Field
    registration_instance_id = models.ManyToManyField(Registration_instance)


class Registration_instance_has_event_gift(models.Model):
    registration_instance_id = models.ForeignKey(Registration_instance)
    event_gift_id = models.ForeignKey(Event_gift)
    amount = models.PositiveIntegerField(default=0)