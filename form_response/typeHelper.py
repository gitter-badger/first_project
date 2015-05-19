
from django import forms


def convert_string_to_type(type):

    if(type == "Number"):
        return forms.FloatField()
    if(type == "txt"):
        return forms.CharField(max_length=55)
