from django.contrib import admin

from beauty_salon_manage_sistem.accounts.forms import AppProfileEditForm
from beauty_salon_manage_sistem.accounts.models import AppStaffProfile, AppBaseUser, AppCustomerUser

@admin.register(AppBaseUser)
class AppBaseUserAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


# @admin.register(AppStaffProfile)
# class AppStaffProfileAdmin(admin.ModelAdmin):
#     # form = AppProfileEditForm
#     fields = ('first_name', 'last_name', 'position',)


@admin.register(AppCustomerUser)
class AppCustomerUserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'phone_number', 'date_of_join',]
    ordering = ['first_name', '-date_of_join',]
