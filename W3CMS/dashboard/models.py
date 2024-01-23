from django.db import models


class Configurations(models.Model):
    INPUT_TYPE_CHOICES = (
        ('','Select InputType'),
        ('text','text'),
        ('textarea','textarea'),
        ('file','file'),
        ('checkbox','checkbox'),
        ('radio','radio'),
        ('button','button'),
        ('select','select'),
    )
    name = models.CharField(max_length=255,null=True)
    value = models.CharField(max_length=255, null=True,blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    input_type = models.CharField(max_length=255,choices=INPUT_TYPE_CHOICES, default=INPUT_TYPE_CHOICES[0][0])
    editable = models.BooleanField(default=True)
    order=models.IntegerField(null=True,blank=True)
    params =  models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.
    class Meta:
        verbose_name = "configuration"
        verbose_name_plural = "configurations"
    def __str__(self):
        return f'{self.name}'

