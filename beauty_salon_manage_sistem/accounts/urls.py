from django.urls import path, include

from beauty_salon_manage_sistem.accounts.views import ShowAppUsers, CreateAppStaffUser, CreateCustomer, SignInView, \
    SignOutView, AppProfileUpdateView, AppProfileDetailsView

urlpatterns = (
    path('show-users/', ShowAppUsers.as_view(), name='show users'),
    path('register/', CreateAppStaffUser.as_view(), name='register user'),
    path('add-customer/', CreateCustomer.as_view(), name='add customer'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', AppProfileDetailsView.as_view(), name='user details'),
        path('edit/', AppProfileUpdateView.as_view(), name='edit user'),
    ]))
)

# from .signals import *
