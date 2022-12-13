from django.urls import path

from beauty_salon_manage_sistem.common.views import \
    IndexPageWithProfile, index_function_view, InfoPage, search_customers, BookingCreateView, BookingListView, \
    BookingDeleteView

urlpatterns = (
    path('', index_function_view, name='index page'),
    path('sign-in/', IndexPageWithProfile.as_view(), name='index page with profile'),
    path('info-page/', InfoPage.as_view(), name='info page'),
    path('search-customers/', search_customers, name='search customers'),
    path('booking-customer-procedure/', BookingCreateView.as_view(), name='booking customer procedure'),
    path('my-booked-procedures/', BookingListView.as_view(), name='my booking hours'),
    path('delete-booking-procedure/<int:pk>/', BookingDeleteView.as_view(), name='delete booking hour'),
)