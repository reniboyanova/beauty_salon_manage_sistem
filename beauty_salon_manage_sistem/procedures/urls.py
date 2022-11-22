from django.urls import path

from beauty_salon_manage_sistem.procedures.views import AddProcedureToCustomer

urlpatterns = (
        path('add-to-customer/', AddProcedureToCustomer.as_view(), name='add procedure to customer'),
)