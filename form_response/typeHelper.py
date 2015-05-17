from datetimewidget.widgets import DateTimeWidget
from django import forms


def convert_string_to_type(type):
    if(type == "CharField"):
        return forms.CharField(max_length=55)
    elif(type == "Number"):
        return forms.FloatField()
    elif(type == "DateTimeField"):
        return forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
