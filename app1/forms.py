from django import forms


class UserRegistrarForm(forms.Form):
    nombre = forms.CharField()
    fono = forms.CharField()
    email = forms.CharField()