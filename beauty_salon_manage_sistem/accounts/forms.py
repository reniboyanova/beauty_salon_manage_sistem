from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppStaffProfile
from beauty_salon_manage_sistem.core.validators import validate_only_letters

UserModel = get_user_model()


class RegistrationAppUserForm(UserCreationForm):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 40

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 40

    MAX_LEN_POSITION = 100

    first_name = forms.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ],
        widget=forms.TextInput(attrs={'placeholder': 'First name'}),
        required=True,
    )

    last_name = forms.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Last name'}),
        required=True,
    )

    position = forms.CharField(
        max_length=MAX_LEN_POSITION,
        widget=forms.TextInput(attrs={'placeholder': 'Position'}),
        required=True,
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password',
        })
    )

    class Meta:
        model = UserModel
        fields = ('email', )
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': 'Enter your email',
            }),

        }
        labels = {
            'email': 'Email:',
        }

    def cleaned_data_fist_name(self):
        return self.cleaned_data['first_name']

    def cleaned_data_last_name(self):
        return self.cleaned_data['last_name']

    def cleaned_data_position(self):
        return self.cleaned_data['position']

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = AppStaffProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            position=self.cleaned_data['position'],
            user=user,
        )
        if commit:
            profile.save()

        return user


class AddingCustomerForm(forms.ModelForm):
    class Meta:
        model = AppCustomerUser
        exclude = ('date_of_join', 'is_staff', 'is_superuser',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name:', 'label': 'Enter your first name:', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name:','class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone number:','class': 'form-control'}),
            'further_explanation': forms.Textarea(attrs={
                'placeholder': 'Additional information:','class': 'form-control'}),

        }



