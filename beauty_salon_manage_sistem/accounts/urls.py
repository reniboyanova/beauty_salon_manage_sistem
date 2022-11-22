from django.urls import path

from beauty_salon_manage_sistem.accounts.views import ShowAppUsers, CreateAppStaffUser, CreateCustomer

urlpatterns = (
    path('show-users/', ShowAppUsers.as_view(), name='show users'),
    path('register/', CreateAppStaffUser.as_view(), name='register user'),
    path('add-customer/', CreateCustomer.as_view(), name='add customer'),
)

# from .signals import *