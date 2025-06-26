from django import forms
from .models import Location, Rentals, Image


class RentalForm(forms.ModelForm):

    class Meta:
        model = Rentals
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
