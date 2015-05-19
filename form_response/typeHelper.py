
from django import forms


def convert_string_to_type(type):

    if type == "Number":
        return forms.FloatField(widget=forms.FloatField(attrs={'class': 'form-control'}))
    if type == "txt":
        return forms.CharField(max_length=55,widget=forms.TextInput(attrs={'class': 'form-control'}))
