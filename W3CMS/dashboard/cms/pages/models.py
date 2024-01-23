from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField 


def user_directory_path(instance, filename):
	return f'pages/{instance.slug}/feature_image/{filename}'

class Page(MPTTModel):
    PAGE_TYPE_CHOICES = (
        ('Page','Page'),
        ('Widget','Widget')
    )
    PAGE_STATUS_CHOICES = (
        ('Published','Published'),
        ('Draft','Draft'),
        ('Pending','Pending')
    )
    PAGE_VISIBILITY_CHOICES = (
        ('Pu','Public'),
        ('PP','Password Protected'),
        ('Pr','Private')
    )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    user_id = models.IntegerField()
    type = models.CharField(max_length=255, choices=PAGE_TYPE_CHOICES, default=PAGE_TYPE_CHOICES[0][0])
    title = models.CharField(max_length=255, blank=False)
    content = RichTextUploadingField(null=True,blank=True)
    slug = models.SlugField(max_length=255,unique=True, null=True)
    excerpt = models.TextField(null=True,blank=True)
    comment = models.BooleanField(default=True)
    password = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255, choices=PAGE_STATUS_CHOICES, default=PAGE_STATUS_CHOICES[0][0])
    visibility = models.CharField(max_length=255, choices=PAGE_VISIBILITY_CHOICES, default=PAGE_VISIBILITY_CHOICES[0][0])
    feature_image = models.ImageField(upload_to=user_directory_path,max_length=500,default="default/default.jpg")
    publish_on = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        order_with_respect_to = 'publish_on'


    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.slug}'


# Add Custom Fields
class PageMeta(models.Model):
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    value =  models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.
    
    class Meta:
        verbose_name = "Page Meta"
        verbose_name_plural = "Page Metas"

    def __str__(self):
        return self.name


class PageSeo(models.Model):
    page = models.OneToOneField(Page,on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=255, null=True)
    meta_keywords = models.CharField(max_length=500,blank=True,null=True)
    meta_descriptions = models.TextField(blank=True, null=True)
    content_url = models.URLField(max_length=255, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.

    
    class Meta:
        verbose_name = "Page Seo"
        verbose_name_plural = "Page Seos"

    def __str__(self):
        return self.title