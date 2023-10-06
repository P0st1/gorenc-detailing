from django import forms
from django.forms import inlineformset_factory
from .models import KontaktStranka, Avto

class KontaktObrazec(forms.ModelForm):
    class Meta:
        model = KontaktStranka
        fields = ['ime', 'email', 'telefonska_stevilka', 'vas_avto', 'sporocilo']

