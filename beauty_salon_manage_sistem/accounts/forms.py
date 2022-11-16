from django import forms
from django.contrib.auth.forms import UsernameField, UserCreationForm

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppStaffUser


class CreateAppCustomerUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password'
        })
    )
    class Meta:
        model = AppCustomerUser
        exclude = ['username', ]
        fields = ('first_name', 'last_name', 'password1', 'password2', 'email', 'gender', 'hair_long', 'hair_type', 'further_explanation', 'phone_number',)
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'value': '+359',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Your first name:',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name:',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Enter your email:',
            }),

        }
        # field_classes = {"username": UsernameField}


class CreateAppStaffUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password'
        })
    )
    exclude = ('username',)

    class Meta:
        model = AppStaffUser
        exclude = ['username', ]
        fields = ('first_name', 'last_name', 'email', 'position',)
