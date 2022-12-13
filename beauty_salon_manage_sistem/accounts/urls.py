from django.urls import path, include

from beauty_salon_manage_sistem.accounts.views import ShowAppCustomers, CreateAppStaffUser, CreateCustomer, SignInView, \
    SignOutView, AppStaffProfileUpdateView, AppStaffProfileDetailsView, AppCustomerProfileDeleteView, \
    AppCustomerProfileUpdateView, SuperUserProfileDetailsView, ShowCurrentCustomerProcedure, \
    CreateAppStaffUserFromManager

urlpatterns = (
    path('show-users/', ShowAppCustomers.as_view(), name='show customers'),
    path('register/', CreateAppStaffUser.as_view(), name='register user'),
    path('add-staff/', CreateAppStaffUserFromManager.as_view(), name='add staff'),
    path('add-customer/', CreateCustomer.as_view(), name='add customer'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', AppStaffProfileDetailsView.as_view(), name='my profile details'),
        path('edit/', AppStaffProfileUpdateView.as_view(), name='edit user'),
        path('superuser/', SuperUserProfileDetailsView.as_view(), name='superuser details')
    ])),
    path('customer/<int:pk>/', include([
        path('delete/', AppCustomerProfileDeleteView.as_view(), name='delete customer profile'),
        path('edit/', AppCustomerProfileUpdateView.as_view(), name='edit customer profile'),
        path('procedures/', ShowCurrentCustomerProcedure.as_view(), name='all customer procedures'),
    ])),
)

# from .signals import *
