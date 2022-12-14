from django.urls import path

from beauty_salon_manage_sistem.products.views import ProductDetailsView, AddProductView, ProductDeleteView, \
    ProductUpdateView

urlpatterns = (
    path('', ProductDetailsView.as_view(), name='detail product'),
    path('add/', AddProductView.as_view(), name='add product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit product'),
)