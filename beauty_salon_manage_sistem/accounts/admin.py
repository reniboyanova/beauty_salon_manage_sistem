from django.contrib import admin

from beauty_salon_manage_sistem.accounts.forms import AppUserEditForm, AppProfileEditForm, RegistrationAppUserForm
from beauty_salon_manage_sistem.accounts.models import AppStaffProfile, AppBaseUser


# Now register the new UserAdmin.
@admin.register(AppBaseUser)
class AppBaseUserAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


@admin.register(AppStaffProfile)
class AppStaffProfileAdmin(admin.ModelAdmin):
    form = AppProfileEditForm
    fields = ('first_name', 'last_name', 'position',)
