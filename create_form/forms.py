from django import forms

required_fields = ["inputCategory",
"inputDescription",
"inputEventTitle",
"inputFrom",
"inputFromTime",
"inputLocation",
"inputMaxParticipants",
"inputPrice",
"inputTo",
"inputToTime",
"optionsRadios",
"inputCheckbox"]


class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        d = args[0]
        super(MyForm, self).__init__(*args, **kwargs)
        for key in d:
            required=False
            if key in required_fields:
                required = True
            if "Amount" in key or "MaxParticipants":
                self.fields[key] = forms.IntegerField(required=required)
            elif "FromTime" in key or "ToTime" in key:
                self.fields[key] = forms.TimeField(required=required)
            elif "From" in key or "To" in key:
                self.fields[key] = forms.DateField(required=required)
            else:
                self.fields[key] = forms.CharField(required=required)
            self.fields[key] = forms.CharField(required=required)
