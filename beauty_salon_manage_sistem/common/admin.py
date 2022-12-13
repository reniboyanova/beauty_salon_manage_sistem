from django.contrib import admin

from beauty_salon_manage_sistem.common.models import BookingCustomerProcedure


@admin.register(BookingCustomerProcedure)
class BookingProcedureAdmin(admin.ModelAdmin):
    list_display = ['select_date', 'select_time', 'hair_stylist', 'customer', ]
    ordering = ['-select_date', 'select_time', ]
