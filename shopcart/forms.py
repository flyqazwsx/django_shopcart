from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # 設定
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
