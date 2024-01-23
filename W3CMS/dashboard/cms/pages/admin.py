from django.contrib import admin 
from dashboard.cms.pages.models import Page, PageMeta, PageSeo
from mptt.admin import DraggableMPTTAdmin
#pages/admin.py



@admin.register(Page)
class PageAdminConfig(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('indented_title',)
    

@admin.register(PageMeta)
class PageMetaAdminConfig(admin.ModelAdmin):
    list_display = ("id","page","name", "value", "created_at", "updated_at")
    list_display_links = ('page',)


@admin.register(PageSeo)
class PageSeoAdminConfig(admin.ModelAdmin):
    list_display = ("title", "meta_keywords", "created_at", "updated_at")
    list_display_links = ('title',)

