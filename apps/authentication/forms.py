from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, password_validation

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ActorSignUpForm(forms.Form):
    choices = (
        ("faculty", "faculty"),
        ("department heads", "department heads"),
        ("research coordinator", "research coordinator"),
        ("extension coordinator", "extension coordinator")
    )
    profile_picture = forms.FileField()
    username = forms.CharField(label="Username", max_length=255)
    first_name = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)
    email_address = forms.EmailField(label="Email Address")
    address = forms.CharField(label="Address", max_length=255)
    birthday = forms.DateField(label="Birthday", widget=DateInput)
    contact = forms.CharField(label="Contact No. ", max_length=255)
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Enter your new password",
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    account_type = forms.ChoiceField(choices=choices)

    class Meta:
        model = User
        fields = ['username','profile_picture', 'first_name','last_name','username', 'email_address', 'address', 'birthday', 'contact',
                  'password1', 'password2', 'account_type']


class AdminSignUpForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=255)
    middle_name = forms.CharField(label="Middle Name (optional)", max_length=255, required=False)
    last_name = forms.CharField(label="Last Name", max_length=255)
    email_address = forms.EmailField(label="Email Address")
    address = forms.CharField(label="Address", max_length=255)
    birthday = forms.DateField(label="Birthday", widget=DateInput)
    contact = forms.CharField(label="Contact No. ", max_length=255)
    employee_no = forms.CharField(label="Employee No. ", max_length=255)
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        exclude = ['username']
        fields = ['first_name', 'middle_name', 'last_name', 'email_address', 'address', 'birthday', 'contact', 'employee_no',
                  'password1', 'password2']


class ResetPassword(forms.Form):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class" : "form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class" : "form-control"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )