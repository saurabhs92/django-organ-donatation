from django import forms

from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            'name',
            'email',
            'phone',
            'dob',
            'living',
            'organ',
        ]
