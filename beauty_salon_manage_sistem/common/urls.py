from django.urls import path

from beauty_salon_manage_sistem.common.views import \
    IndexPageWithProfile, index_function_view, InfoPage

urlpatterns = (
    path('', index_function_view, name='index page'),
    path('sign-in/', IndexPageWithProfile.as_view(), name='index page with profile'),
    path('info-page/', InfoPage.as_view(), name='info page'),
)