from django.contrib import admin

from beauty_salon_manage_sistem.products.models import AddProducts


@admin.register(AddProducts)
class AddProductsAdmin(admin.ModelAdmin):
    list_display = ['brand', 'type_of_product', 'serial_number',]
    search_fields = ['type_of_product', 'serial_number']