from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import TextInput, EmailInput, PasswordInput
User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control", 'placeholder': "Email"}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Nom d'utilisateur"
            }),
            'password1': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Mot de passe'
            }),
            'password2': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Confirmez le mot de passe'
            })
        }