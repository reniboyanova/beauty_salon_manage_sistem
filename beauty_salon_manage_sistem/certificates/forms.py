from django import forms

from beauty_salon_manage_sistem.certificates.models import ProfessionalCertificate


class DateInputType(forms.DateInput):
    input_type = 'date'


class CreateCertificateForm(forms.ModelForm):
    class Meta:
        model = ProfessionalCertificate
        fields = '__all__'
        widgets = {
            'date_of_certificate': DateInputType(),
            'valid_until': DateInputType(),
            }

