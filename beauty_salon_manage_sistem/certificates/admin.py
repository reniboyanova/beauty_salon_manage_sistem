from django.contrib import admin

from beauty_salon_manage_sistem.certificates.forms import CreateCertificateForm
from beauty_salon_manage_sistem.certificates.models import ProfessionalCertificate


@admin.register(ProfessionalCertificate)
class ProfessionalCertificateAdmin(admin.ModelAdmin):
    add_form = CreateCertificateForm
    list_display = ['date_of_certificate', 'valid_until', 'certificate_owner', 'qualification']
    ordering = ['date_of_certificate', 'valid_until',]
