from django.db import models
from django.conf import settings
# Create your models here.

class Subscribes(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True) 
    name =  models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=False)
    unsubscribe = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.
    class Meta:
        verbose_name = "subscriber"
        verbose_name_plural = "subscribers"
    def __str__(self):
        return f'{self.email}'