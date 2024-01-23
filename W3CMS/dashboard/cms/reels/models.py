from django.db import models
from django.conf import settings
from dashboard.cms.blog.models import Blogs
from mptt.models import MPTTModel,TreeForeignKey,TreeManyToManyField

class Video(models.Model):
 
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')  # This will upload videos to the 'media/videos/' directory.
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title