from django import forms
from .models import Foods

class FoodsForm(forms.ModelForm):
    class Meta:
        model= Foods
        fields= ["food", "calories"]
