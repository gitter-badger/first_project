from datetimewidget.widgets import DateTimeWidget
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.forms import forms


class RegistrationForm(forms.Form):
    class Meta:
        widgets = {
            'datetime': DateTimeWidget(usel10n=True, bootstrap_version=3)
        }


# class EventDetails(models.Model):
#     def __init__(self, event_id, title, category, status, max_participants, current_participants_amount, price, location, date_from, date_to,
#                  description):
#         self.event_id = event_id
#         self.description = description
#         self.date_to = date_to
#         self.date_from = date_from
#         self.location = location
#         self.price = price
#         self.current_participants_amount = current_participants_amount
#         self.max_participants = max_participants
#         self.status = status
#         self.category = category
#         self.title = title
#
#     title = models.CharField(max_length=1000)
#     category = models.CharField(max_length=1000)
#     event_id = models.AutoField(primary_key=True)
#     status = models.CharField(max_length=1000)
#     max_participants = models.PositiveIntegerField()
#     current_participants_amount = models.PositiveIntegerField()
#     price = models.FloatField()
#     location = models.CharField(max_length=1000)
#     date_from = models.DateTimeField()
#     date_to = models.DateTimeField()
#     description = models.CharField(max_length=1000)
#
#
# class FormField():
#     def __init__(self, name, mandatory, type):
#         self.name = name
#         self.mandatory = mandatory
#         self.type = type
#
#     name = models.CharField(max_length=55)
#     type = models.CharField(max_length=55)
#     mandatory = models.BooleanField(default=False)


class Registration_instance(models.Model):
    registration_instance_id = models.AutoField(primary_key=True)
    event_assesment = models.FloatField(validators=[MinValueValidator(1.0),MaxValueValidator(5.0)])
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