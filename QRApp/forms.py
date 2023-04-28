import qrcode
from django import forms
from .models import Qrlink
import tempfile


class QrlinkForm(forms.ModelForm):
    class Meta:
        model = Qrlink
        fields = "__all__"



class GenerarQrForm(forms.ModelForm):
    class Meta:
        model = Qrlink
        fields = ['link', 'titulo']

    def save(self, commit=True):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.cleaned_data['link'])
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        with tempfile.NamedTemporaryFile(delete=False) as f:
            img.save(f, format='PNG')
            f.flush()
            instance = super().save(commit=False)
            instance.qr.save('qr.png', f, save=False)
        if commit:
            instance.save()
        return instance
