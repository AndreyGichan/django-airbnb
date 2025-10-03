from django import forms

from .models import Property

class PropertyForm(forms.ModelForm):
    image_file = forms.FileField(required=False)
    class Meta:
        model = Property
        fields = (
            'title',
            'description',
            'price_per_night',
            'bedrooms',
            'bathrooms',
            'guests',
            'country',
            'country_code',
            'category'
        )