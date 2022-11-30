from django.urls import path, include

from beauty_salon_manage_sistem.procedures.views import AddProcedureToCustomer, ShowAllCustomersProcedure

urlpatterns = (
    path('add-to-customer/', AddProcedureToCustomer.as_view(), name='add procedure to customer'),
    path('customer-procedures/<int:pk>/', include([
        path('', ShowAllCustomersProcedure.as_view(), name='procedures of customer'), ], ), )
)
