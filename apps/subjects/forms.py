from django import forms
from django.db.models import Q

from apps.authentication.models import Actor
from apps.subjects.models import Subjects


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, subjects):
        return "%s" % subjects.title


# creating a form
class SubjectsForm(forms.ModelForm):
    subjects = CustomMMCF(queryset=Subjects.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Actor
        fields = ['subjects']

    def __init__(self, user=None, **kwargs):
        super(SubjectsForm, self).__init__(**kwargs)
        if user:
            self.fields['subjects'].queryset = Subjects.objects.filter(~Q(faculty_subjects__user=user))


class NewSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"
