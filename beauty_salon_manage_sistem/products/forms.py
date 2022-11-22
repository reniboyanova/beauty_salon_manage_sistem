from django import forms

from beauty_salon_manage_sistem.products.models import TypeOfProducts


class AddProductForm(forms.ModelForm):
    class Meta:
        model = TypeOfProducts
        fields = '__all__'
