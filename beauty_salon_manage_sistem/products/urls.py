from django.urls import path

from beauty_salon_manage_sistem.products.views import ProductDetailsView, AddProductView

urlpatterns = (
    path('', ProductDetailsView.as_view(), name='detail product'),
    path('add/', AddProductView.as_view(), name='add product'),
)