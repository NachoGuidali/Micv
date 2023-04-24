from django import forms
from .models import Qrlink

class QrlinkForm(forms.ModelForm):
    class Meta:
        model = Qrlink
        fields = "__all__"