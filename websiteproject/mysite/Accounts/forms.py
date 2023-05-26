from django import forms

class TherapistForm(forms.Form):
    firstname = forms.CharField(max_length=60)
    lastname= forms.CharField(max_length=60)