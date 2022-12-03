from django.urls import path

from beauty_salon_manage_sistem.common.views import IndexPageView, IndexPageWithProfile

urlpatterns = (
    path('', IndexPageView.as_view(), name='index page'),
    path('sign-in/', IndexPageWithProfile.as_view(), name='index page with profile'),
)