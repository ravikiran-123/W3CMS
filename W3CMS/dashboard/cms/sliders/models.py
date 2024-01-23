from django.db import models
from django.conf import settings
from dashboard.cms.blog.models import Blogs
from mptt.models import MPTTModel,TreeForeignKey,TreeManyToManyField

# Create your models here.
class Slider(models.Model):
    title=models.CharField(max_length=50,blank=True,null=True)
    slider_image=models.ImageField(blank=True,null=True,upload_to='slider_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title