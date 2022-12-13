from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from beauty_salon_manage_sistem.certificates.forms import CreateCertificateForm


class AddProfessionalCertificateView(LoginRequiredMixin, CreateView):
    template_name = 'certificates/add_professional_certificate.html'
    form_class = CreateCertificateForm
    success_url = reverse_lazy('add certificate')