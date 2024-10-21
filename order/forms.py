#forms.py
from django import forms
from .models import Item, ItemImage, Item2, ItemImage2, Item3, ItemImage3


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name_item', 'description', 'image', 'video', 'area_in_meters', 'room', 'kitchen', 'bathroom', 'hall', 'Plakona']
        labels = {
            'name_item': 'Item Name',
            'description': 'Description',
            'image': 'Item Image',
            'area_in_meters': 'Area (m²)',
            'room': 'Number of Rooms',
            'kitchen': 'Number of Kitchens',
            'bathroom': 'Number of Bathrooms',
            'hall': 'Number of Halls',
            'Plakona': 'Number of Balconies',
        }

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']


class ItemForm2(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ['name_item', 'description', 'image', 'video', 'area_in_meters']
        labels = {
            'name_item': 'Item Name',
            'description': 'Description',
            'image': 'Item Image',
            'area_in_meters': 'Area (m²)',

        }

class ItemImageForm2(forms.ModelForm):
    class Meta:
        model = ItemImage3
        fields = ['image']



class ItemForm3(forms.ModelForm):
    class Meta:
        model = Item3
        fields = ['name_item', 'description', 'image', 'video', 'area_in_meters']
        labels = {
            'name_item': 'Item Name',
            'description': 'Description',
            'image': 'Item Image',
            'area_in_meters': 'Area (m²)',
        }

class ItemImageForm3(forms.ModelForm):
    class Meta:
        model = ItemImage3
        fields = ['image']