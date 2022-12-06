from django.urls import path, include

from beauty_salon_manage_sistem.procedures.views import AddProcedureToCustomer, ShowAllCustomersProcedure, \
    ProceduresDetailsView, ProcedureDetailView

urlpatterns = (
    path('add-to-customer/', AddProcedureToCustomer.as_view(), name='add procedure to customer'),
    path('all-beauty-salon-procedures/', ProceduresDetailsView.as_view(), name='all beauty salon procedures'),
    path('procedure-information/<int:pk>/', ProcedureDetailView.as_view(), name='full information for procedure'),
    path('all-customer-procedures/<int:pk>/', include([
        path('', ShowAllCustomersProcedure.as_view(), name='procedures of customer'),

    ], ),),)
