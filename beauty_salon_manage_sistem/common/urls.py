from django.urls import path

from beauty_salon_manage_sistem.common.views import IndexPageView

urlpatterns = (
    path('', IndexPageView.as_view(), name='index page'),
)