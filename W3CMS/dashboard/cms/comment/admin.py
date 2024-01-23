from django.contrib import admin
from dashboard.cms.comment.models import Comment
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Comment, MPTTModelAdmin)