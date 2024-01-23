from django.db import models
from django.conf import settings
from dashboard.cms.blog.models import Blogs
from mptt.models import MPTTModel,TreeForeignKey,TreeManyToManyField

# Create your models here.
class Comment(MPTTModel):

    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('spam', 'Spam'),
        ('trash', 'Trash'),
    )


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True,)
    post = models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='children')
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='approved')


    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.name