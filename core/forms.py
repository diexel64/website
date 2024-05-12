from django import forms
from django.contrib.auth.models import User
from .models import Profile, Valoracion


class ValoracionForm(forms.ModelForm):
    valoracion = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)])
    class Meta:
        model = Valoracion
        fields = ['comentario', 'valoracion']
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

