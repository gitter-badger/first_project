from datetimewidget.widgets import DateTimeWidget
from django.db import models

# Create your models here.
from django.forms import forms


class RegistrationForm(forms.Form):
    class Meta:
        widgets = {
            'datetime': DateTimeWidget(usel10n=True, bootstrap_version=3)
        }


class EventDetails(models.Model):
    def __init__(self, event_id, title, category, status, max_participants, current_participants_amount, price, location, date_from, date_to,
                 description):
        self.event_id = event_id
        self.description = description
        self.date_to = date_to
        self.date_from = date_from
        self.location = location
        self.price = price
        self.current_participants_amount = current_participants_amount
        self.max_participants = max_participants
        self.status = status
        self.category = category
        self.title = title

    title = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    event_id = models.PositiveIntegerField()
    status = models.CharField(max_length=1000)
    max_participants = models.PositiveIntegerField()
    current_participants_amount = models.PositiveIntegerField()
    price = models.FloatField()
    location = models.CharField(max_length=1000)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    description = models.CharField(max_length=1000)


class FormField():
    def __init__(self, name, mandatory, type):
        self.name = name
        self.mandatory = mandatory
        self.type = type

    name = models.CharField(max_length=55)
    type = models.CharField(max_length=55)
    mandatory = models.BooleanField(default=False)
