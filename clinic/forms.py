
from django import forms
from .models import patient
from django.forms import TextInput, CharField


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ('__all__')                      #('photo', 'id', 'date', 'name', 'sex', 'age', 'weight', 'mobile_number', 'Complain', 'medical_history', 'BP', 'PR', 'SPO2', 'Advice', 'prescription')

   