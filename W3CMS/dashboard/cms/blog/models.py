from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField 
from django.conf import settings
from mptt.models import MPTTModel,TreeForeignKey,TreeManyToManyField
from django.utils.translation import gettext_lazy as _ 

class Categories(MPTTModel):
    title = models.CharField(max_length=255, blank=False,unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255,unique=True, null=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.
    class MPTTMeta:
        verbose_name = _('Category')
        verbose_name_plural = "Categories"
       
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def _str_(self):
        return self.title
    

class Tags(models.Model):
    name = models.CharField(max_length=255,unique=True,blank=False)
    slug = models.SlugField(max_length=255,unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

    def _str_(self):
        return self.name


def user_directory_path(instance, filename):
	return f'blog/{instance.slug}/feature_image/{filename}'

class Blogs(models.Model):
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, blank=False)
    content = RichTextUploadingField(null=True,blank=True)
    excerpt = models.TextField(null=True,blank=True)
    slug = models.SlugField(max_length=255,unique=True, null=True)
    comment = models.BooleanField(default=True)
    password = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255, choices=PAGE_STATUS_CHOICES, default=PAGE_STATUS_CHOICES[0][0])
    visibility = models.CharField(max_length=255, choices=PAGE_VISIBILITY_CHOICES, default=PAGE_VISIBILITY_CHOICES[0][0])
    publish_on = models.DateField(blank=True, null=True)
    categories = TreeManyToManyField(Categories, blank=True)
    tags = models.ManyToManyField(Tags,blank=True)
    views= models.IntegerField(default=0)
    feature_image = models.ImageField(upload_to=user_directory_path,max_length=500, default="default/default.jpg")
    video_url = models.URLField(null=True,blank=True,help_text="YouTube Embed URL")
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        order_with_respect_to = 'publish_on'

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def _str_(self):
        return self.slug


class Metas(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    value = models.TextField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.
    
    class Meta:
        verbose_name = "Meta"
        verbose_name_plural = "Metas"

    def _str_(self):
        return f'{self.blog.title}'
    
# class video_url(models.Model):
#     url = models.TextField(blank=False, null=False)
#     blog = models.ForeignKey(Blogs,on_delete=models.CASCADE, null=True)
  
    # class Meta:
        # verbose_name = "Video_url"
        # verbose_name_plural = "Video_urls"

    def _str_(self):
        return f'{self.blog.title}'

class Seo(models.Model):
    title = models.CharField(max_length=255)
    blog = models.OneToOneField(Blogs,on_delete=models.CASCADE, primary_key=True)
    meta_keywords = models.CharField(max_length=500,blank=True,null=True)
    meta_descriptions = models.TextField(blank=True, null=True)
    blog_url = models.URLField(max_length=255, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.
    
    class Meta:
        verbose_name = "Seo"
        verbose_name_plural = "Seos"

    def _str_(self):
        return self.title