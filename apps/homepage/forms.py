from django import forms

from apps.authentication.models import Departments, User


class DepartmentForm(forms.ModelForm):
    headed_by = forms.ModelChoiceField(queryset=User.objects.filter(is_faculty=True))

    class Meta:
        model = Departments
        fields = ['department', 'headed_by']
