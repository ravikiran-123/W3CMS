from django import forms
from .models import Slider
from mptt.forms import TreeNodeChoiceField  # If you're using MPTT

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'  # You can specify specific fields if needed
