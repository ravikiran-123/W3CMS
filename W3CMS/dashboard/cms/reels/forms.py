# reels/forms.py

from django import forms
from .models import Video
from mptt.forms import TreeNodeChoiceField  # If you're using MPTT

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'  # You can specify specific fields if needed
