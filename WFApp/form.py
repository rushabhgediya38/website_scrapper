from django import forms
from .models import freq


class freq_form(forms.ModelForm):
    class Meta:
        model = freq
        fields = [
            'freq_url',
        ]
