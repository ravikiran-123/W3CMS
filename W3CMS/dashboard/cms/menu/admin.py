from django.contrib import admin
from dashboard.cms.menu.models import  Menus, Items
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


class ItemsInlineAdmin(admin.TabularInline):
    model = Items
    extra=2
      
class MenusAdmin(admin.ModelAdmin):
    inlines = [ItemsInlineAdmin]
    prepopulated_fields = {"slug": ("title",)}
    


class ItemAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)

    
admin.site.register(Menus,MenusAdmin)
admin.site.register(Items,ItemAdmin)
