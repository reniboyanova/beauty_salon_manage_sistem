from django.urls import path, include

from beauty_salon_manage_sistem.accounts.views import ShowAppUsers, CreateAppStaffUser, CreateCustomer, SignInView, \
    SignOutView, AppStaffProfileUpdateView, AppStaffProfileDetailsView, AppCustomerProfileDeleteView, \
    AppCustomerProfileUpdateView, SuperUserProfileDetailsView

urlpatterns = (
    path('show-users/', ShowAppUsers.as_view(), name='show users'),
    path('register/', CreateAppStaffUser.as_view(), name='register user'),
    path('add-customer/', CreateCustomer.as_view(), name='add customer'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', AppStaffProfileDetailsView.as_view(), name='user details'),
        path('edit/', AppStaffProfileUpdateView.as_view(), name='edit user'),
        path('superuser/', SuperUserProfileDetailsView.as_view(), name='superuser details')
    ])),
    path('customer/<int:pk>/', include([
        path('delete/', AppCustomerProfileDeleteView.as_view(), name='delete customer profile'),
        path('edit/', AppCustomerProfileUpdateView.as_view(), name='edit customer profile'),
    ])),
)

# from .signals import *
