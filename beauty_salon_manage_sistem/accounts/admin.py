from django.contrib import admin

from beauty_salon_manage_sistem.accounts.forms import RegistrationAppUserForm, AppProfileEditForm, AppUserEditForm
from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppBaseUser, AppStaffProfile


@admin.register(AppBaseUser)
class AppBaseUserAdmin(admin.ModelAdmin):
    add_form = RegistrationAppUserForm
    form = AppProfileEditForm
    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)

@admin.register(AppStaffProfile)
class AppStaffProfileAdmin(admin.ModelAdmin):
    form = AppUserEditForm
    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)

@admin.register(AppCustomerUser)
class AppCustomerUserAdmin(admin.ModelAdmin):
    pass

# TODO fix the admin vision!
