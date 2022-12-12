from django.urls import path

from beauty_salon_manage_sistem.certificates.views import AddProfessionalCertificateView

urlpatterns = (
    path('certificates/', AddProfessionalCertificateView.as_view(), name='add certificate'),
)