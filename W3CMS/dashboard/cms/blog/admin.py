from django.contrib import admin
from dashboard.cms.blog.models import Blogs, Categories, Tags, Metas, Seo

from mptt.admin import DraggableMPTTAdmin



class MetasInlineAdmin(admin.TabularInline):
    model = Metas

class BlogAdmin(admin.ModelAdmin):
    inlines = [MetasInlineAdmin]
    prepopulated_fields = {"slug": ("title",)}
    


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    prepopulated_fields = {"slug": ("title",)}
    

admin.site.register(Categories, CategoryAdmin2)

admin.site.register(Blogs,BlogAdmin)

admin.site.register(Metas)
admin.site.register(Tags)

admin.site.register(Seo)


