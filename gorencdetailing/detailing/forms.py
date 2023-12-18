from django import forms
from .models import KontaktStranka, Storitev

class KontaktObrazec(forms.ModelForm):
    class Meta:
        model = KontaktStranka
        fields = '__all__'

    storitev = forms.ModelMultipleChoiceField(
        queryset=Storitev.objects.all(),
        widget=forms.Select,
    )

