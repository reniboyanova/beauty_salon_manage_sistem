from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppStaffProfile
from beauty_salon_manage_sistem.common.models import BookingCustomerProcedure
from beauty_salon_manage_sistem.core.validators import validate_only_letters
from beauty_salon_manage_sistem.procedures.models import Procedure

UserModel = get_user_model()


# Registration App User with adding Profile
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
        error_messages=(),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password',
        }),
        error_messages=(),
        label='Repeat Password'
    )

    class Meta:
        model = UserModel
        fields = ('email',)
        exclude = ('is_active', 'is_staff', 'is_superuser', 'date_joined')
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': 'Enter your email',
            }),

       }

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


# Adding Customer form. This is NOT a registration form!
class AddingCustomerForm(forms.ModelForm):
    class Meta:
        model = AppCustomerUser
        exclude = ('date_of_join', 'is_staff', 'is_superuser',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'col-sm-5 col-form-label'}),
            'last_name': forms.TextInput(attrs={
                'class': 'col-sm-5 col-form-label'}),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+359123456789', 'class': 'col-sm-5 col-form-label',}),
            'further_explanation': forms.Textarea(attrs={
                'placeholder': 'Add more information about customer'}),
            'hair_type': forms.Select(attrs={'class': 'col-sm-5 col-form-label', }),
            'hair_stylist': forms.CheckboxSelectMultiple(),
            'hair_long': forms.Select(attrs={'class': 'col-sm-5 col-form-label', }),
            'gender': forms.Select(attrs={'class': 'col-sm-5 col-form-label', }),

        }


class AppProfileEditForm(RegistrationAppUserForm):
    class Meta:
        model = AppStaffProfile
        exclude = ('email', 'password1', 'password2',)


class AppUserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email', )


class AppProfileDeleteForm(AddingCustomerForm):
    class Meta:
        model = AppCustomerUser
        fields = ()

    def save(self, commit=True):
        if commit:
            Procedure.objects \
                .all() \
                .delete()
            BookingCustomerProcedure.objects.all().delete()
            self.instance.delete()

        return self.instance


class AppCustomerEditForm(AddingCustomerForm):
    pass


# class AppUserDeleteForm(RegistrationAppUserForm):
#     class Meta:
#         model = UserModel
#
#     def save(self, commit=True):
#         if commit:
#             AppStaffProfile.objects.filter(user=self.instance).delete()
#             self.instance.delete()
#
#         return self.instance