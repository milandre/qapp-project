"""User Forms.

This file has the forms used
for user operations like
login and reistration.
"""

from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User


class RegisterForm(auth_forms.UserCreationForm):
    """RegisterForm

    A form for user registration. Inherit from
    UserCreationForm
    """

    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Email',
                                                            'required': 'required'
                            }))

    class Meta(auth_forms.UserCreationForm):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
