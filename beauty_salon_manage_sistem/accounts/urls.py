from django.urls import path

from beauty_salon_manage_sistem.accounts.views import ShowAppUsers, CreateAppCustomerUser, CreateAppStaffUser

urlpatterns = (
    path('show-users/', ShowAppUsers.as_view(), name='show users'),
    path('register/', CreateAppCustomerUser.as_view(), name='register user'),
    path('register/staff/', CreateAppStaffUser.as_view(), name='register staff'),
)