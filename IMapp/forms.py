from django.db.models.base import Model
from django.forms import ModelForm, fields, widgets
from .models import ProductModel, LocationModel
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'

        widgets = {
            'location': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'})
        }

class LocationForm(ModelForm):
    class Meta:
        model = LocationModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
