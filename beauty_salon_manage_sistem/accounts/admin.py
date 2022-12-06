from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from beauty_salon_manage_sistem.accounts.forms import RegistrationAppUserForm, AppProfileEditForm, AppUserEditForm
from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppBaseUser, AppStaffProfile


@admin.register(AppStaffProfile)
class AppBaserUser(UserAdmin):
    add_form = RegistrationAppUserForm
    # form = AppUserEditForm
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password',
                ),
            }),


        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)


