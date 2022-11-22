from django.contrib import admin

from beauty_salon_manage_sistem.products.models import AddProducts


@admin.register(AddProducts)
class AddProductsAdmin(admin.ModelAdmin):
    pass