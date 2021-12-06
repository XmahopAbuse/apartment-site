from .models import Application

from django import forms

import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'placeholder': '8(999)123-45-67', 'name':'phone'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Ваше имя', 'name':'name'})
        self.fields['date_start'].widget.attrs.update({'name':'startdate', 'type':'date'})
   
    class Meta:

        model = Application
        fields = ("phone", "name", "date_start", "date_end")
        widgets = {
            'date_start': DateInput(),
            'date_end': DateInput()
        }
