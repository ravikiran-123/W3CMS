from django.contrib import admin
from dashboard.cms.reels.models import Video
from mptt.admin import MPTTModelAdmin


admin.site.register(Video,MPTTModelAdmin)