from django import forms

from beauty_salon_manage_sistem.procedures.models import Procedure


class AddProcedureToCustomerForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'
        widgets = {
            'comment_about_haircut': forms.Textarea(attrs={
                'rows': 3,
                'cols': 90
            }),
            'comment_about_styling': forms.Textarea(attrs={
                'rows': 3,
                'cols': 90
            }),
            'product_used_for_color': forms.Textarea(attrs={
                'rows': 3,
                'cols': 90
            }),
            'product_used_for_treatment': forms.Textarea(attrs={
                'rows': 3,
                'cols': 90
            }),
            'other_comments': forms.Textarea(attrs={
                'rows': 3,
                'cols': 90
            }),
        }
