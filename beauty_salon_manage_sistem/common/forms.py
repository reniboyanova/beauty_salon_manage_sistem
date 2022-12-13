from django import forms

from beauty_salon_manage_sistem.common.models import BookingCustomerProcedure


class DateInputType(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingCustomerProcedure
        fields = '__all__'
        widgets = {
            'select_date': DateInputType(),
        }


class BookingFormDeleteForm(BookingForm):
    class Meta:
        model = BookingCustomerProcedure
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
