#forms.py
from django import forms
from .models import Item, ItemImage, Item2, ItemImage2, Item3, ItemImage3


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name_item', 'description', 'image', 'video', 'area_in_meters', 'room', 'kitchen', 'bathroom', 'hall', 'Plakona']
        labels = {
            'name_item': 'اسم العنصر',
            'description': 'الوصف',
            'image': 'صورة العنصر',
            'area_in_meters': 'المساحة (م²)',
            'room': 'عدد الغرف',
            'kitchen': 'عدد المطابخ',
            'bathroom': 'عدد الحمامات',
            'hall': 'عدد الصالات',
            'Plakona': 'عدد البلكونات',
        }
        # إضافة الـ placeholders
        widgets = {
            'name_item': forms.TextInput(attrs={'placeholder': 'أدخل اسم الوحدة', 'required': 'required'}),
            'description': forms.Textarea(attrs={'placeholder': 'اكتب وصفًا جيدًا للوحدة هنا', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'required': 'required'}),
            'video': forms.ClearableFileInput(attrs={'required': 'required'}),
            'area_in_meters': forms.NumberInput(attrs={'placeholder': 'أدخل المساحة بالمتر مربع', 'required': 'required'}),
            'room': forms.NumberInput(attrs={'placeholder': 'أدخل عدد الغرف', 'required': 'required'}),
            'kitchen': forms.NumberInput(attrs={'placeholder': 'أدخل عدد المطابخ', 'required': 'required'}),
            'bathroom': forms.NumberInput(attrs={'placeholder': 'أدخل عدد الحمامات', 'required': 'required'}),
            'hall': forms.NumberInput(attrs={'placeholder': 'أدخل عدد الصالات', 'required': 'required'}),
            'Plakona': forms.NumberInput(attrs={'placeholder': 'أدخل عدد البلكونات', 'required': 'required'}),
        }

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': 'required'}),
        }

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
        widgets = {
            'name_item': forms.TextInput(attrs={'placeholder': 'أدخل اسم الوحدة', 'required': 'required'}),
            'description': forms.Textarea(attrs={'placeholder': 'اكتب وصفًا جيدًا للوحدة هنا', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'required': 'required'}),
            'video': forms.ClearableFileInput(attrs={'required': 'required'}),
            'area_in_meters': forms.NumberInput(attrs={'placeholder': 'أدخل المساحة بالمتر مربع', 'required': 'required'}),

        }
        

class ItemImageForm2(forms.ModelForm):
    class Meta:
        model = ItemImage3
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': 'required'}),
        }



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

        widgets = {
            'name_item': forms.TextInput(attrs={'placeholder': 'أدخل اسم الوحدة', 'required': 'required'}),
            'description': forms.Textarea(attrs={'placeholder': 'اكتب وصفًا جيدًا للوحدة هنا', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'required': 'required'}),
            'video': forms.ClearableFileInput(attrs={'required': 'required'}),
            'area_in_meters': forms.NumberInput(attrs={'placeholder': 'أدخل المساحة بالمتر مربع', 'required': 'required'}),

        }

class ItemImageForm3(forms.ModelForm):
    class Meta:
        model = ItemImage3
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': 'required'}),
        }
