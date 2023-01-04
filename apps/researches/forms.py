from django import forms

from .models import *


class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ['document', 'title', 'summary', 'status']