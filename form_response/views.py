from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_http_methods
from create_form.models import Event, OwnField
from form_response.models import RegistrationForm, RegistrationInstance, FormFieldInstance
from form_response.typeHelper import convert_string_to_type
from datetime import datetime
import create_form.models as CreateForm

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    #Pobierz event
    # user_1 = User.objects.create_user("test")
    # event_status_1 = CreateForm.Status(name="open")
    # event_status_1.save()
    # event_category_1 = CreateForm.Category(name="Mountains")
    # event_category_1.save()
    # event_4 = CreateForm.Event(id=1, user=User.objects.get(id=user_1.id), status=event_status_1, category=event_category_1,
    #                            title="Title",
    #                            max_participants=1, price=2.5, location="Krakow", start_date=datetime.now(),
    #                            end_date=datetime.now(), description="Description")
    # event_4.save()
    # file_type = CreateForm.FileType( file_type="txt")
    # file_type.save()
    # file_type = CreateForm.FileType( file_type="Number")
    # file_type.save()
    # own_field = CreateForm.OwnField(title="Title1", description="Description1", field_type="txt", event=CreateForm.Event.objects.get(id=1))
    # own_field.save()
    # own_field = CreateForm.OwnField(title="Title2", description="Description2", field_type="Number", event=CreateForm.Event.objects.get(id=1))
    # own_field.save()
    # own_field = CreateForm.OwnField(title="Title3", description="Description3", field_type="txt", event=CreateForm.Event.objects.get(id=1))
    # own_field.save()
    # own_field = CreateForm.OwnField(title="Title4", description="Description4", field_type="txt", event=CreateForm.Event.objects.get(id=1))
    # own_field.save()
    event_id = request.GET["id"]
    event = Event.objects.get(id=event_id)
    form_fields_list = OwnField.objects.filter(event=event)
    attrs = {}
    attrs.__setitem__("name", forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={"required":"required", 'class': 'form-control', "placeholder": "Enter your name"})))
    attrs.__setitem__("lastName", forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={"required":"required", 'class': 'form-control', "placeholder": "Enter your lastname"})))
    attrs.__setitem__("email", forms.EmailField(required=True, validators=[validate_email], widget=forms.EmailInput(attrs={"required":"required",'class': 'form-control', "placeholder": "Enter your email"})))
    for field in form_fields_list:
        attrs.__setitem__(field.title, convert_string_to_type(field.field_type))

    form = type("RegistrationForm", (RegistrationForm,), attrs)
    return render(request, 'register.html', {'event': event, 'form': form})

@require_http_methods(["POST"])
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    # Stworz instancje rejestracji
    # Stworz instancje formularzy
    Myform = RegistrationForm(request.POST)
    if Myform.is_valid():
        event = Event.objects.get(id=request.POST.get("eventId"))
        registration_instance = RegistrationInstance(event=event, name=request.POST.get("name"), last_name=request.POST.get("lastName"), email=request.POST.get("email"))
        registration_instance.save()
        form_fields_list = OwnField.objects.filter(event=event)

        for field in form_fields_list:
            FormFieldInstance(form_field=field,registration_instance=registration_instance,value=request.POST.get(field.title)).save()
        response= HttpResponseRedirect('/form_response/success/')
        return response
    else:
        return render(request, 'registration_failed.html', {'registration_failure_reason':'because form was wrongly fulfilled'})

def success(request):
    return render(request, 'registration_successful.html')