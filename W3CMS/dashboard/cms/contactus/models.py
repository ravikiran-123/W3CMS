from django.db import models
from django.core.validators import RegexValidator


class ContactUs(models.Model):
   
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, unique=True, null=True)
    message = models.TextField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)# Validators should be a list
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.

    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email