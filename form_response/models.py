from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.forms import forms
from create_form.models import Event, OwnField, Gift


class RegistrationForm(forms.Form):
    pass


class RegistrationInstance(models.Model):
    event_assessment = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    event_fraudulent = models.BooleanField(default=False)
    registration_confirmed = models.BooleanField(default=False)
    event = models.ForeignKey(Event)
    gifts = models.ManyToManyField(Gift, through='RegistrationInstanceGifts', blank=True, null=True)


class FormFieldInstance(models.Model):
    form_field = models.ForeignKey(OwnField)
    value = models.CharField(max_length=1000)
    registration_instance = models.ForeignKey(RegistrationInstance)


class RegistrationInstanceGifts(models.Model):
    registration_instance = models.ForeignKey(RegistrationInstance)
    gift = models.ForeignKey(Gift)
    amount = models.PositiveIntegerField(default=0)