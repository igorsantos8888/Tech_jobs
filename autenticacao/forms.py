from dataclasses import fields
from django import forms
from .models import UserJob

class UserJobForm(forms.ModelForm):
    class Meta:
        model = UserJob
        fields = '__all__'