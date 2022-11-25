from django import forms

from beauty_salon_manage_sistem.products.models import AddProducts


class AddProductForm(forms.ModelForm):
    class Meta:
        model = AddProducts
        fields = ('brand', 'grams', 'type_of_product', 'image_of_product', 'serial_number')
        widgets = {
            'brand': forms.Select(),
            'grams': forms.NumberInput(attrs={
                'placeholder': '1000',
            }),
            'image_of_product': forms.URLInput(attrs={
                'placeholder': 'Image URL',
            }),
            'serial_number': forms.NumberInput(attrs={
                'initial': '#'
            }),

        }

