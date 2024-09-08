from django import forms
from base.models.address_model import AddressModel




class AdressForm(forms.ModelForm):
 class Meta:
    model= AddressModel
    fields="__all__"
    exclude = ("is_deleted",)