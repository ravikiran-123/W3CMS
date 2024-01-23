from django.contrib import admin
from dashboard.cms.sliders.models import Slider
from mptt.admin import MPTTModelAdmin


admin.site.register(Slider,MPTTModelAdmin)