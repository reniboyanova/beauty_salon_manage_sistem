from django.contrib import admin

from beauty_salon_manage_sistem.accounts.models import AppStaffUser, AppCustomerUser


@admin.register(AppStaffUser)
class AppStaffUserAdmin(admin.ModelAdmin):
    pass


@admin.register(AppCustomerUser)
class AppCustomerUserAdmin(admin.ModelAdmin):
    pass

# TODO fix the admin vision!
