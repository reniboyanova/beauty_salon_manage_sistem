from django.contrib import admin

from beauty_salon_manage_sistem.accounts.models import AppCustomerUser, AppBaseUser, AppStaffProfile


@admin.register(AppBaseUser)
class AppBaseUserAdmin(admin.ModelAdmin):
    pass

@admin.register(AppStaffProfile)
class AppStaffProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(AppCustomerUser)
class AppCustomerUserAdmin(admin.ModelAdmin):
    pass

# TODO fix the admin vision!
