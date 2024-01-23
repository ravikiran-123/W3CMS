from django import forms
from dashboard.cms.contactus.models import ContactUs


class ContactusForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ( 
                  'name',
                  'email',
                  'phone',
                  'message',
                  )