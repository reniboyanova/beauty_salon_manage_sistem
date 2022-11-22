from django import forms

from beauty_salon_manage_sistem.procedures.models import Procedure


class AddProcedureToCustomerForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'
