from django import forms
from .models import UserJob
from django.core.validators import RegexValidator

class UserJobForm(forms.ModelForm):
    
    #! validators
    
    nome = forms.CharField(
        label = 'Nome', min_length= 3, max_length= 255,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message = "Somente letras podem ser inclusas!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nome'}),
    )
    class Meta:
        model = UserJob
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'telefone'}),
            'Data de Nascimento': forms.TextInput(attrs={'placeholder': '26/06/1997'}),
            'senha': forms.TextInput(attrs={'placeholder': 'senha', 'type':'password'})
        }
    
    
    