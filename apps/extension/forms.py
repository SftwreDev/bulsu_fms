from django import forms

from apps.extension.models import Extension


class ExtensionForm(forms.ModelForm):
    class Meta:
        model = Extension
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
        }