from django import forms
from dashboard.models import Configurations






class ConfigurationForm(forms.ModelForm):
    
    class Meta:
        model = Configurations
        fields = ( 
                  'name',
                  'value',
                  'title',
                  'description',
                  'input_type',
                  'editable',
                  'params'
                  )
                    